import mysql.connector as Myconn

mydb = Myconn.connect(host="localhost",user="root",password="admin")

db_cursor = mydb.cursor()
db_cursor.execute("create database khwaja")
print("Database Created")