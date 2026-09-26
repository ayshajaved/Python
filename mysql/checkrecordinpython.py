import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database = "Learningmysql")
db_cursor = mydb.cursor()
db_cursor.execute("select * from employee")
# db_record = db_cursor.fetchall()
# print(db_record)                            #records are printed

#but to print in loop
for db_record in db_cursor.fetchall():
    print(db_record)      

#if we use fetchone , one record will e displayed