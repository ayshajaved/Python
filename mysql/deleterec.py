# import mysql.connector as ms
# mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database = "Learningmysql")
# db_ = mydb.cursor()
# db_delete = "delete from employee where name = %s"
# db_value = ("maheen",)
# db_.execute(db_delete, db_value)
# mydb.commit()
# #deleted

#in order to delete the entire table records
import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database = "Learningmysql")
db_ = mydb.cursor()
db_delete = "truncate table employee"
db_.execute(db_delete)
mydb.commit()

#table deleted
