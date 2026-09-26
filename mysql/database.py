import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//")
db_cursor = mydb.cursor()        #mydb has the method cursor that is used to create the database
db_cursor.execute("create database Learningmysql")              #db_cursor has method execute to create the databse