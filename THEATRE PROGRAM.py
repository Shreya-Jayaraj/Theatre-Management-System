import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kpo123',database='ams_theatre')
mycursor=mydb.cursor()
while True:
    print()
    print("*"*70)
    print("*                                                                    *")
    print("*          Welcome to AMS Movie Ticket Booking System                *")
    print("*                                                                    *")
    print("*"*70)
    print("\nEnter E if you wish to exit the program.")
    ac= input("Are you a Customer or an Admin: (C/A/E) ")


    if ac.upper() == 'C':
        
        while True:
            print("\n","-"*77)
            print("\n", "MENU")
            print("1. To book movie tickets. ")
            print("2. To view details of a prebooked ticket.")
            print("3. To cancel your ticket booking.")
            print("4. To become an AMS PLATINUM CARD HOLDER.")
            print("5. To view your AMS PLATINUM CARD.")
            print("6. To return to Home page.")
            print("\n","-"*77)
            print()
            ch=int(input("ENTER CHOICE : "))
            print()

            
            if ch==1:
                print("-------------------------------------")
                print("| NOTE: Cost of each ticket is Rs.150 |")
                print("-------------------------------------")
                mycursor.execute("SELECT max(Ticket_No) FROM ticket_history;")
                data=mycursor.fetchall()
                tno=int(data[0][0])+1
                cname=input("Enter your name: ")
                print('\nSelect the number corresponding to your choice. ')
                mycursor.execute("SELECT MS_No,Movie_Name FROM movies")
                
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="   ")
                    print()
                mydb.commit()
                
                x=int(input("\nEnter movie number: "))
                for i in data:
                    if i[0]==x:
                        mname=i[1]
                        
                mdate=input("Enter date: ")
                qty= int(input("\nEnter the number of tickets: "))
                amount = qty*150
                email = input('\nEnter your Email ID: ')
                
                yn = input('\nDo you wish to order any food items? (Y/N) ')
                if yn.upper() == 'Y':
                    print('Select the number corresponding to your choice. ')
                    mycursor.execute("SELECT AS_No,Food_Beverage,Cost FROM add_ons")
                    print("\n","-"*77)
                    print( "MENU".center(70))
                    print('Sizes Available for all items: S|M|L'.center(70))
                    
                    data=mycursor.fetchall()
                    for i  in data:
                        print(i[0], i[1], sep=' ')
                        print('Cost (S|M|L) :',i[2])
                        print()
                    print("\n","-"*77)
                    mydb.commit()
                    print()
                    
                    y = int(input('Enter number: '))
                    s = input('Enter size: ')
                    for i in data:
                        if i[0]==y:
                            add=i[1]+' ('+s+')'
                            print('Additional Cost for add-ons to be paid at the theatre.')
                else:
                    add = 'NULL'
                print('\nTotal Amount to be paid: ', amount)
                print()
                print('Please proceed to make payment.')
                print('''| NOTE: WE WILL NOT IN ANY CIRCUMSTANCE SHARE YOUR PERSONAL INFORMATION WITH OTHER
INDIVIDUALS OR ORGANISATIONS WITHOUT YOUR PERMISSION |''')
                print()
                pay= int(input("\nEnter your card number: "))
                print("PAYMENT SUCCESSFUL")
                mycursor.execute("INSERT INTO ticket_history VALUES('"+str(tno)+"','"+cname+"','"+mname+"','"+str(mdate)+"','"+str(qty)+"','"+str(amount)+"','"+email+"','"+add+"')")
                mydb.commit()
                print('********TICKET BOOKING SUCCESSFULL!********'.center(70))
                print('\n(Ticket summary will be sent to the registered Email ID.)')
                print('THANK YOU! ENJOY YOUR MOVIE EXPERIENCE.')

                
            elif ch==2:
                tno = int(input('Enter ticket number: '))
                mycursor.execute("SELECT * FROM ticket_history WHERE Ticket_No=%s"%(tno,))
                
                data=mycursor.fetchall()
                if data==[]:
                    print("TICKET NOT FOUND!")
                else:
                    print("\n","-"*77)
                    print("TICKET SUMMARY".center(70))
                    print()
                    for i in data:
                        print('  Ticket No =',i[0])
                        print('  Movie Name: '+i[2])
                        print('  Movie Date: '+str(i[3]))
                        print("  Ticket Holder: "+i[1])
                        print("  No of tickets: "+str(i[4]))
                        print('  Email ID: '+i[6])
                        print('  Amount Paid: '+str(i[5]))
                        if i[7]==None:
                            print('  Add-ons: NIL')
                        else:
                            print('  Add-ons: '+i[7])
                        print("\n","-"*77)
                        
                mydb.commit()


            elif ch==3:
                tno = int(input('Enter Ticket No: '))
                mycursor.execute("SELECT * FROM ticket_history WHERE Ticket_No=%s"%(tno,))
                data = mycursor.fetchall()
                if data==[]:
                    print("Invalid ticket number")
                else:
                    mycursor.execute("DELETE FROM ticket_history WHERE Ticket_No=%s"%(tno,))
                    print("Your booking has been cancelled successfully.".center(70))
                    mydb.commit()


            elif ch==4:
                from datetime import date
                print("-----------------------------------------------------")
                print("| NOTE: Cost for issuing AMS PLATINUM card is Rs.300 |")
                print("-----------------------------------------------------")
                mycursor.execute("SELECT max(Card_No) FROM membership;")
                data=mycursor.fetchall()
                mbno=int(data[0][0])+1
                mbname=input("Enter your name: ")
                date = date.today()
                email= input("Enter Email_ID: ")
                mycursor.execute("INSERT INTO membership VALUES('"+str(mbno)+"','"+mbname+"','"+str(date)+"','"+email+"')")
                print('\nTotal Amount to be paid: 300')
                print()
                print('Please proceed to make payment.')
                print('''| NOTE: WE WILL NOT IN ANY CIRCUMSTANCE SHARE YOUR PERSONAL INFORMATION WITH OTHER
INDIVIDUALS OR ORGANISATIONS WITHOUT YOUR PERMISSION |''')
                print()
                pay= int(input("\nEnter your card number: "))
                print("PAYMENT SUCCESSFUL")
                print('\n','WELCOME TO THE AMS PLATINUM CLUB!!!'.center(70))
                print('Your card has been issued successfully.'.center(70))
                print('Thank you for joining us.'.center(70))
                print('\n(Card summary will be sent to the registered Email ID.)')
                mydb.commit()


            elif ch==5:
                mbno=input("Enter your card number : ")
                mycursor.execute("SELECT * FROM membership WHERE Card_No=%s"%(mbno,))
                data=mycursor.fetchall()
                if data==[]:
                    print("INVALID CARD NUMBER.")
                else:
                    print("\n","-"*77)
                    print("AMS PLATINUM CARD".center(70))
                    print()
                    for i in data:
                        print('  Card No =',i[0])
                        print('  Card Holder: '+i[1])
                        print('  Issue Date: '+str(i[2]))
                        print('  Email ID: '+i[3])
                    print("\n","-"*77)
                mydb.commit()

                        
            elif ch==6:
                print("RETURNING TO HOME PAGE!")
                break


            else:
                print('Please enter valid option.')

        
    elif ac.upper() == 'A':
        
        while True:
            print("\n","-"*77)
            print("\n", "MENU")
            print("1. To print a ticket. ")
            print("2. To view AMS Platinum card details of a member.")
            print("3. To add a new movie to the Movies table.")
            print("4. To add a new food item to the Add_ons table.")
            print("5. To view the movies table.")
            print("6. To view the Add_ons table.")
            print("7. To delete a movie from Movies table.")
            print("8. To delete an item from Add_ons table ")
            print("9. To cancel membership. ")
            print("10. To return to Home page.")
            print("\n","-"*77)
            print()
            ch=int(input("ENTER CHOICE : "))
            print()
            

            if ch==1:
                tno = int(input('Enter ticket number of the customer: '))
                mycursor.execute("SELECT * FROM ticket_history WHERE Ticket_No='%s'"%(tno,))
                
                data=mycursor.fetchall()
                if data==[]:
                    print("TICKET NOT FOUND!")
                else:
                    print("\n","-"*77)
                    print("TICKET SUMMARY".center(70))
                    print()
                    for i in data:
                        print('  Ticket No =',i[0])
                        print('  Movie Name: '+i[2])
                        print('  Movie Date: '+str(i[3]))
                        print("  Ticket Holder: "+i[1])
                        print("  No of tickets: "+str(i[4]))
                        print('  Email ID: '+i[6])
                        print('  Amount Paid: '+str(i[5]))
                        if i[7]==None:
                            print('  Add-ons: NIL')
                        else:
                            print('  Add-ons: '+i[7])
                        print("\n","-"*77)

            elif ch==2:
                mbno=input("Enter customer card number : ")
                mycursor.execute("SELECT * FROM membership WHERE Card_No=%s"%(mbno,))
                data=mycursor.fetchall()
                if data==[]:
                    print("INVALID CARD NUMBER.")
                else:
                    print("\n","-"*77)
                    print("AMS PLATINUM CARD".center(70))
                    print()
                    for i in data:
                        print('  Card No =',i[0])
                        print('  Card Holder: '+i[1])
                        print('  Issue Date: '+str(i[2]))
                        print('  Email ID: '+i[3])
                    print("\n","-"*77)
                    
                
            elif ch==3:
                mycursor.execute("SELECT max(MS_No) FROM Movies;")
                data=mycursor.fetchall()
                mno=int(data[0][0])+1
                mname=input("Enter movie name: ")                        
                ar=input("Enter age rating: ")
                lang= input("Enter the language: ")
                dur = input('Enter the duration of the movie: ')       
                showt = input('Enter the showtime of the movie: ')
                mycursor.execute("INSERT INTO Movies VALUES('"+str(mno)+"','"+mname+"','"+ar+"','"+lang+"','"+str(dur)+"','"+showt+"')")
                mydb.commit()
                print('********MOVIE ADDED SUCCESSFULLY!********'.center(70))

            elif ch==4:
                mycursor.execute("SELECT max(AS_No) FROM Add_ons;")
                data=mycursor.fetchall()
                AS_no=int(data[0][0])+1
                fbname=input("Enter food/beverage : ")                        
                size=input("Enter size(S|M|L) : ")
                cost= int(input("Enter the cost: "))
                mycursor.execute("INSERT INTO Add_ons VALUES('"+str(AS_no)+"','"+fbname+"','"+size+"','"+str(cost)+"')")
                mydb.commit()
                print('********ITEM ADDED SUCCESSFULLY!********'.center(70))

            elif ch==5:
                print()
                mycursor.execute("SELECT * FROM Movies;")
                data=mycursor.fetchall()
                for i in data:
                    print(i[0],'|',i[1]," "*(16-len(str(i[1]))),end='')
                    for j in range(2,len(i)):
                        print('|',i[j]," "*(11-len(str(i[j]))),end='')
                    print()
                mydb.commit()

                
            elif ch==6:
                print()   
                mycursor.execute("SELECT * FROM Add_ons;")
                data=mycursor.fetchall()
                for i in data:
                    print(i[0],'|',i[1]," "*(10-len(str(i[1]))),end='')
                    for j in range(2,len(i)):
                        print('|',i[j]," "*(5-len(str(i[j]))),end='')
                    print()
                mydb.commit()

            elif ch==7:
                mno = int(input('Enter the movie number: '))
                mycursor.execute("SELECT * FROM movies WHERE MS_No='%s'"%(mno,))
                data = mycursor.fetchall()
                if data==[]:
                    print("Invalid movie number")
                else:
                    mycursor.execute("DELETE FROM movies WHERE MS_No=%s"%(mno,))
                    print("The movie has been deleted successfully.".center(70))
                    mydb.commit()
                    
                mycursor.execute("SELECT COUNT(*) FROM movies")
                data=mycursor.fetchall()
                for i in data:
                    print("Total no. of movies: ", i[0])
                mydb.commit()
                
        
            elif ch==8:
                ano = int(input('Enter the item number: '))
                mycursor.execute("SELECT * FROM add_ons WHERE AS_No='%s'"%(ano,))
                data = mycursor.fetchall()
                if data==[]:
                    print("Invalid item number")
                else:
                    mycursor.execute("DELETE FROM add_ons WHERE AS_No=%s"%(ano,))
                    print("The item has been deleted successfully.".center(70))
                    mydb.commit()
                mycursor.execute("SELECT COUNT(*) FROM add_ons")
                data=mycursor.fetchall()
                for i in data:
                    print("Total no. of add_ons: ", i[0])
                mydb.commit()
                

            elif ch==9:
                mbno = int(input('Enter your card number: '))
                mycursor.execute("SELECT * FROM membership WHERE Card_No=%s"%(mbno,))
                data = mycursor.fetchall()
                if data==[]:
                    print("Invalid card number")
                else:
                    mycursor.execute("DELETE FROM membership WHERE Card_No=%s"%(mbno,))
                    print("Your card has been cancelled successfully.".center(70))
                    mydb.commit()
                mycursor.execute("SELECT COUNT(*) FROM membership")
                data=mycursor.fetchall()
                if data==[]:
                    print("\nNo members yet!")
                else:
                    for i in data:
                        print("Total no. of members: ", i[0])
                mydb.commit()


            elif ch==10:
                print("RETURNING TO HOME PAGE!")
                break

            else:
                print('Please enter valid option.')
                
          
    elif ac.upper()=='E':
        break

    else:
        print('\nPlease enter valid option.')
