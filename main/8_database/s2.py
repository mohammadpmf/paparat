import pymysql

connection = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = connection.cursor()
query = "CREATE DATABASE IF NOT EXISTS `aparat_test`;"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS `aparat_test`.`users` (\
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,\
  `username` VARCHAR(45) NOT NULL,\
  `password` VARCHAR(45) NOT NULL,\
  PRIMARY KEY (`id`),\
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,\
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);\
"
cursor.execute(query)
message = "Press 1 to Login\nPress 2 to create account\nPress 3 to update your password\nPress 4 to delete account\nPress 0 to exit\n:"
answer = input(message)
while answer not in ['1', '2', '3', '4', '0']:
    answer = input(message)
if answer =='0':
    exit()
elif answer=='2':
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "INSERT INTO `aparat_test`.`users` (`username`, `password`) VALUES (%s, %s);"
    values = username, password
    cursor.execute(query, values)
    connection.commit()
elif answer=='3':
    username = input("Enter username: ")
    old_password = input("Enter your old password: ")
    new_password = input("Enter your new password: ")
    query = "SELECT * FROM `aparat_test`.`users` WHERE username=%s;"
    values = username
    cursor.execute(query, values)
    item = cursor.fetchone()
    previous_password = item[2]
    if previous_password == old_password:
        query = "UPDATE `aparat_test`.`users` SET `password` = 'alavi2' WHERE (`id` = %s);"
        values=item[0]
        cursor.execute(query, values)
        connection.commit()
elif answer=='4':
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "SELECT * FROM `aparat_test`.`users` WHERE username=%s;"
    values = username
    cursor.execute(query, values)
    item = cursor.fetchone()
    previous_password = item[2]
    if previous_password == password:
        query = "DELETE FROM `aparat_test`.`users` WHERE (`id` = %s);"
        values = item[0]
        cursor.execute(query, values)
        connection.commit()

connection.close()
