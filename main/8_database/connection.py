import pymysql

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

    def __del__(self):
        if self.check_connection():
            self.connection.close()


