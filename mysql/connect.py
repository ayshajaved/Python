import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//")
if mydb.is_connected():
    print("Connection established!!")
    