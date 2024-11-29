import mysql.connector as Myconn
# age = int(input("Enter age :"))
# name = (input("Enter name :"))
mydb = Myconn.connect(host="localhost",user="root",password="admin",database="khwaja")

# #update from database
# db_cursor = mydb.cursor()
# db_update = "update emp set roll=%s where name=%s"
# db_value = (19,"hussain")
# db_cursor.execute(db_update,db_value)
# mydb.commit()
# print("updated")


#delete data from database
db_cursor = mydb.cursor()
db_delete = "delete from emp where name=%s"
db_value = ("khwaja",)
db_cursor.execute(db_delete,db_value)
mydb.commit()
print(db_cursor.rowcount,"deleted")



#insert value in database
# query ="insert into emp values (%s,%s)"
# # values = [(33,"frre"),(44,"lool"),(55,"new")]
# value = (77,'ddd')
# db_cursor.execute(query,value)
# db_cursor.execute("select * from khwaja.emp")
# db_select=db_cursor.fetchone()
# for i in db_cursor.fetchall():
#     print(i)
# mydb.commit()
# print(db_select)
# print(db_cursor.rowcount,"record inserted")


# for i in db_cursor:
#     print(i)
# print("Table Created")