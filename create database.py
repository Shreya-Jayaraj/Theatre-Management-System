import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kpo123')
mycursor=mydb.cursor()

mycursor.execute('Create database ams_theatre')

