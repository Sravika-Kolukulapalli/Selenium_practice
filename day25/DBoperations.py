#insert,update,delete
insert_query='insert into student values(101,"vineela")'
insert_query='insert into student values(102,"prasanna")'
update_query="update student set sname='sravika' where sid=100"
delete_query="delete from student where sid=102"
import mysql.connector

try:
    connection=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="Cisco1@11042002",database="db")
    curs=connection.cursor()#create cursor
    # curs.execute(insert_query)#execute query through cursor
    # curs.execute(update_query)
    curs.execute(delete_query)
    connection.commit()#commit transaction
    connection.close()
except:
    print("connection unsuccessful")

print("Finished.......")



