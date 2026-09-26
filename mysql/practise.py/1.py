import mysql.connector as ms
db = ms.connect(user = "root", password = "sql#@$678*&*&//", host = "localhost")
db_cursor = db.cursor()
# db_cursor.execute("show databases")
# for i in db_cursor:
#     print(i)

db_cursor.execute("use ayesha")
# db_cursor.execute("show tables")
# for i in db_cursor:
#     print(i)

db_cursor.execute("select * from institute")
for i in db_cursor:
    print(i)

db_cursor.execute("insert into institute (name, place) values (%s, %s)", ("ucp", "lhr"))
db.commit()