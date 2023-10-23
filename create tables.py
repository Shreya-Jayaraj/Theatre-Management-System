import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kpo123',database='ams_theatre')
mycursor=mydb.cursor()


mycursor.execute("create table Movies\
        (MS_No integer primary key not null, \
        Movie_Name varchar(40),\
        Age_Rating varchar(15),\
        Language varchar(20),\
        Duration time,\
        Show_Time varchar(20))")

mycursor.execute("create table Ticket_History \
        (Ticket_No integer primary key not null, \
        Customer_Name varchar(30),\
        Movie_Name varchar(40),\
        Movie_Date date,\
        Ticket_Qty integer,\
        Amount_Paid decimal(6,2),\
        Email_ID varchar(25),\
        Add_ons varchar(20))")

mycursor.execute("create table Add_ons\
        (AS_No integer primary key not null,\
        Food_Beverage varchar(25),\
        Size_Available varchar(10),\
        Cost integer)")

mycursor.execute("create table Membership \
        (Card_No integer not null primary key, \
        Member_Name varchar(25), \
        Card_Issue_Date date, \
        Email_ID varchar(20))")

mycursor.execute("""insert into Movies
values(1,'Hridayam','G','Malayalam','2:55:00','8am|12pm|6pm'),
(2,'Minnal Murali','G','Malayalam','2:39:00','10am|2pm|10pm'),
(3,'Pushpa: The Rise','PG13','Telugu','2:22:22','11am|3pm|12am')""")

mycursor.execute("""insert into Add_ons
values(1,'Popcorn','S|M|L',40),
(2,'Ice cream','S|M|L',50),
(3,'Coca Cola','S|M|L',25),
(4,'Tea','S|M|L',15),
(5,'Coffee','S|M|L',20)""")

mycursor.execute("""insert into Ticket_History
values(1,'Nikki Abraham','Pushpa: The Rise','2022-02-20',1,150.00,'nikki98@gmail.com','Popcorn(S)')""")

mycursor.execute("""insert into Membership
values(1,'Nikki Abraham','2022-02-20','nikki98@gmail.com')""")
mydb.commit()
