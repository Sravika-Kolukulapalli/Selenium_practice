import mysql.connector
try:
    connection=mysql.connector.connect(host="localhost",port=3306,user="root",password="Cisco1@11042002",database="db")
    curs=connection.cursor()
    curs.execute("select * from student")
    for row in curs:
        print(row[0],row[1])
    connection.close()
except:
    print("connection unsuccessful")

print("finished")