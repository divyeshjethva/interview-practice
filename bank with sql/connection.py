import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bank"
)

cursor = connection.cursor()

cursor.execute("create table if not exists users (id int auto_increment primary key, name varchar(100), balance int)")
connection.commit()