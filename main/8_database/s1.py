import pymysql

connection = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = connection.cursor()
query = "SELECT * FROM `spotify`.`songs`;"
cursor.execute(query)
# for item in cursor.fetchall():
#     print(f"{item[0]} Name: {item[1]} Artist: {item[2]}")
# for item in cursor.fetchmany(10):
#     print(item)
item = cursor.fetchone()
connection.close()