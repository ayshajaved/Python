import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database = "Learningmysql")
db_cursor = mydb.cursor()
db_update  = ("update employee set roll = %s where name = %s")
db_value = (70, "maheen")
db_cursor.execute(db_update, db_value)
mydb.commit()
#updated

