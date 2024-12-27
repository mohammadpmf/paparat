import pymysql
from functions import hash_password

queries = [
    "CREATE SCHEMA IF NOT EXISTS `aparat_game_center`;",
    "CREATE TABLE IF NOT EXISTS `aparat_game_center`.`users` (\
                `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,\
                `name` VARCHAR(45) NULL,\
                `surname` VARCHAR(45) NULL,\
                `username` VARCHAR(45) NOT NULL,\
                `password` VARCHAR(128) NOT NULL,\
                `access_level` TINYINT(1) NOT NULL DEFAULT 2,\
                PRIMARY KEY (`id`),\
                UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,\
                UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);",
    "CREATE TABLE IF NOT EXISTS `aparat_game_center`.`games` (\
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
    "CREATE TABLE IF NOT EXISTS `aparat_game_center`.`orders` (\
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
                    REFERENCES `aparat_game_center`.`users` (`id`)\
                    ON DELETE RESTRICT\
                    ON UPDATE NO ACTION,\
                CONSTRAINT `game`\
                    FOREIGN KEY (`game`)\
                    REFERENCES `aparat_game_center`.`games` (`id`)\
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
        query = "INSERT INTO `aparat_game_center`.`users` (`name`, `surname`, `username`,\
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
        query = "SELECT * FROM `aparat_game_center`.`users` WHERE `username`=%s;"
        values = username
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result==None:
            return -1, "Username does not exist!"
        id, hashed_password, access_level = result[0], result[4], result[5]
        password = hash_password(password, username)
        if password == hashed_password:
            message = f"Welcome {result[1]} {result[2]}"
            return 0, message, access_level
        return -1, "Wrong password!"

    def insert_game(self, name, company, release_date, price, genre, age_range):
        query = "INSERT INTO `aparat_game_center`.`games` (`name`, `company`, `release_date`, `price`,\
              `genre`, `age_range`) VALUES (%s, %s, %s, %s, %s, %s);"
        values = name, company, release_date, price, genre, age_range
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return 0, "OK"
        except pymysql.err.IntegrityError:
            return 2, "Duplicate"
        except pymysql.err.DataError as error:
            if """1366, "Incorrect integer value:""" in str(error):
                return 5, "Age"
            elif """1264, "Out of range value for column 'price""" in str(error):
                return 10, "Price"
            elif """1406, "Data too long for column""" in str(error):
                return 1000, "Long Data"
        return -1, "Unknown Error"

    def __del__(self):
        if self.check_connection():
            self.connection.close()


