import pymysql
from functions import hash_password

queries = [
    "CREATE SCHEMA IF NOT EXISTS `aparat_game_center`;",
    "USE `aparat_game_center`;",
    "CREATE TABLE IF NOT EXISTS `users` (\
                `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,\
                `name` VARCHAR(45) NULL,\
                `surname` VARCHAR(45) NULL,\
                `username` VARCHAR(45) NOT NULL,\
                `password` VARCHAR(128) NOT NULL,\
                `access_level` TINYINT(1) NOT NULL DEFAULT 2,\
                PRIMARY KEY (`id`),\
                UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,\
                UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);",
    "CREATE TABLE IF NOT EXISTS `games` (\
                `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,\
                `name` VARCHAR(45) NOT NULL,\
                `company` VARCHAR(45) NOT NULL,\
                `release_date` DATE NOT NULL,\
                `price` DECIMAL(4,2) NOT NULL DEFAULT 0,\
                `genre` VARCHAR(45) NOT NULL DEFAULT 'other',\
                `age_range` TINYINT(2) UNSIGNED NOT NULL DEFAULT 12,\
                PRIMARY KEY (`id`),\
                UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,\
                UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE);",
    "CREATE TABLE IF NOT EXISTS `orders` (\
                `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,\
                `user` INT UNSIGNED NOT NULL,\
                `game` INT UNSIGNED NOT NULL,\
                `datetime_ordered` DATETIME NOT NULL,\
                PRIMARY KEY (`id`),\
                UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,\
                INDEX `user_idx` (`user` ASC) VISIBLE,\
                INDEX `game_idx` (`game` ASC) VISIBLE,\
                CONSTRAINT `user`\
                    FOREIGN KEY (`user`)\
                    REFERENCES `users` (`id`)\
                    ON DELETE RESTRICT\
                    ON UPDATE NO ACTION,\
                CONSTRAINT `game`\
                    FOREIGN KEY (`game`)\
                    REFERENCES `games` (`id`)\
                    ON DELETE RESTRICT\
                    ON UPDATE NO ACTION);"
]

class Connection():
    def __init__(self, host='127.0.0.1', user='root', password='root'):
        self.host = host
        self.user = user
        self.password = password
        try:
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password)
            self.cursor = self.connection.cursor()
            for query in queries:
                self.cursor.execute(query)
        except:
            pass
    
    def check_connection(self):
        try:
            self.connection
            return True
        except:
            return False
    
    def insert_user(self, username, password, name=None, surname=None):
        query = "INSERT INTO `users` (`name`, `surname`, `username`,\
              `password`, `access_level`) VALUES (%s, %s, %s, %s, '2');"
        hashed_password = hash_password(password, username)
        values = name, surname, username, hashed_password
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return 0, "OK"
        except pymysql.err.IntegrityError:
            return 2, "Duplicate"
    
    def login(self, username, password):
        query = "SELECT * FROM `users` WHERE `username`=%s;"
        values = username
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result==None:
            return -1, "Username does not exist!"
        user_id, hashed_password, access_level = result[0], result[4], result[5]
        password = hash_password(password, username)
        if password == hashed_password:
            message = f"Welcome {result[1]} {result[2]}"
            return 0, message, access_level, user_id
        return -1, "Wrong password!"

    def insert_game(self, name, company, release_date, price, genre, age_range):
        query = "INSERT INTO `games` (`name`, `company`, `release_date`, `price`,\
              `genre`, `age_range`) VALUES (%s, %s, %s, %s, %s, %s);"
        values = name, company, release_date, price, genre, age_range
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return 0, "OK"
        except pymysql.err.IntegrityError:
            return 2, "Duplicate"
    
    def get(self, name):
        query = "SELECT * FROM `games` WHERE `name` = %s;"
        values = name
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result==None:
            return -1, "Game not found!"
        return 0, result

    def delete(self, name):
        result = self.get(name)
        if result[0]==-1:
            return -1, "Game not found!"
        id = result[1][0]
        query = "DELETE FROM `games` WHERE (`id` = %s);"
        values = id
        self.cursor.execute(query, values)
        self.connection.commit()
        return 0, f"Game {name} deleted successfully!"
    
    def update_game(self, name, company, release_date, price, genre, age_range, new_name):
        query = "UPDATE `games` SET `name` = %s, `company` = %s, `release_date` = %s,\
              `price` = %s, `genre` = %s, `age_range` = %s WHERE (`id` = %s);"
        result = self.get(name)
        if result[0]==-1:
            return -1, "Game not found!"
        id = result[1][0]
        if new_name=='':
            new_name=name
        values = new_name, company, release_date, price, genre, age_range, id
        self.cursor.execute(query, values)
        self.connection.commit()
        return 0, f"Game {name} updated successfully!"
    
    def get_all_orders(self):
        query = "SELECT `orders`.`id`,\
        CONCAT(`users`.`name`, ' ', `surname`) AS `full_name`, `username`,\
        `games`.`name` AS `game`, `datetime_ordered` FROM `orders` JOIN `games`\
        ON `orders`.`game`=`games`.`id` JOIN `users`\
        ON `orders`.`user`=`users`.`id`;"
        self.cursor.execute(query)
        resutl = self.cursor.fetchall()
        return resutl
    
    def get_all_orders_of_user_by_id(self, user_id):
        query = "SELECT `orders`.`id`, `name` AS `game`, `price`, `datetime_ordered` FROM `orders`\
              JOIN `games` ON `orders`.`game`=`games`.`id` WHERE `user`=%s;"
        values = user_id
        self.cursor.execute(query, values)
        resutl = self.cursor.fetchall()
        return resutl
    
    def get_all_games(self):
        query = "SELECT * FROM `games`;"
        self.cursor.execute(query)
        resutl = self.cursor.fetchall()
        return resutl

    def search_between_games(self, name, company, date, price_min, price_max, genre, age_range):
        query = "SELECT * FROM `games` WHERE 1=1"
        values = []
        if name:
            query += " AND name LIKE %s"
            values.append(f"%{name}%")
        if company:
            query += " AND company LIKE %s"
            values.append(f"%{company}%")
        if date:
            query += " AND release_date >= %s"
            values.append(date)
        if price_min:
            query += " AND price >= %s"
            values.append(price_min)
        if price_max:
            query += " AND price <= %s"
            values.append(price_max)
        if genre:
            query += " AND genre LIKE %s"
            values.append(f"%{genre}%")
        if age_range:
            query += " AND age_range >= %s"
            values.append(age_range)
        query += ";"
        self.cursor.execute(query, values)
        resutl = self.cursor.fetchall()
        return resutl
    
    def insert_order(self, user, game, datetime_ordered):
        query = "INSERT INTO `orders` (`user`, `game`, `datetime_ordered`) VALUES (%s, %s, %s);"
        values = user, game, datetime_ordered
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return 0, "OK"
        except:
            return -1, "Something went wrong"

    
    def __del__(self):
        if self.check_connection():
            self.connection.close()


