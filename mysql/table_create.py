import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database = "Learningmysql")
db_table = mydb.cursor()
# db_table.execute("create table User(id int, name varchar(20))")
# print("table created!")

#now to check whether the table is created or not
db_table.execute("show tables")
for i in db_table:
    print(i)                   #theres a one table employee

#we can create as many tables we want and then check also
#there are two tables now
#employee and user