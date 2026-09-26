# import mysql.connector as ms
# mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database= "Learningmysql")
# db_record = mydb.cursor()
# db_record.execute ("insert into employee(roll, name) values (%s, %s)", (40, "tehreem"))
# print(db_record.rowcount, "row inserted")
# #if i select query on cmd that select * from Learningmysql.employee;
# #then its empty means no row is inserted
# #we have to commit as below
# mydb.commit()

#now in cmd the row is showing. We can change the value above to insert another row
#there is an another way to do this

# import mysql.connector as ms
# mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database= "Learningmysql")
# db_record = mydb.cursor()
# insert_query = "insert into employee(roll, name) values (%s, %s)"
# insert_value = (50, "ali")
# db_record.execute (insert_query, insert_value)
# print(db_record.rowcount, "row inserted")
# mydb.commit()


#but to insert many rows altogether
import mysql.connector as ms
mydb = ms.connect(host = "localhost", user = "root", password = "mysql678*&*&//", database= "Learningmysql")
db_record = mydb.cursor()
insert_query = "insert into employee(roll, name) values (%s, %s)"
insert_value_list = [(30, "ashr"),(34, "hassan"), (7, "maheen")]
db_record.executemany(insert_query, insert_value_list)
print(db_record.rowcount,"row inserted")
mydb.commit()

#wao

