import mysql.connector as sqlborg
myconn=sqlborg.connect(host='192.168.0.3',user='scenri121',password='scenri121',database='scenri121_project')
while True:
    print("\n\n")
    print("**********STUDENT'S ENROLLMENT SOFTWARE ***********")
    print("1.Enroll Student")
    print("2.View Enrolled Students")
    print("3.Exit")
    choice=input("Enter Choice:")
    if choice=='1':
        print("\n")
        print ("--------WELCOME TO ADMISSION PROCESS--------")
        fn=input ("enter first name:")
        ln=input ("enter last name:")
        age=int(input ("enter age:"))
        sex=input ("enter sex:")
        per=float(input("enter percentage:"))

        print("\n")
           
        cursorob=myconn.cursor()
        query="""select *
                 from streams;"""
        cursorob.execute(query)
        x=cursorob.fetchall()
        c=cursorob.rowcount
        for row in x:
            print(row)

        print("\n\n")
        print("which stream you want to opt for , please choose from the above option either 1,2 or 3 and enter your choice below")
        ch=input("enter your choice :")
        print("\n\n")
        if ch=="1" :
            if per>=50 and per<=100:
                sid=int(input("enter ID:"))
                print (fn,"well done you have been admitted")
                print ("now choose your subjects")
                print("\n")
                cursorob=myconn.cursor()
                query="""select * from subject_comb where s_id =1 order by s_id;"""
                cursorob.execute(query)
                x=cursorob.fetchall()
                c=cursorob.rowcount
                for row in x:
                    print(row)
                print("\n")
                ch1=input("enter your choice (A,B,C,D) :")
                if ch1=="A":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'A_art')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="B":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'B_art')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="C":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'C_art')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="D":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'D_art')
                    cursorob.execute(query)
                    myconn.commit()
                else:
                    print("the entered choice is not in the given option")          
            
            else:
                print("you are not eligible since required percentage is not met ")
        if ch=="2" :
            if per>=70 and per<=100:
                sid=int(input("enter ID:"))
                print (fn,"well done you have been admitted")
                print ("now choose your subjects")
                print("\n")
                cursorob=myconn.cursor()
                query="""select * from subject_comb where s_id =2;"""
                cursorob.execute(query)
                x=cursorob.fetchall()
                c=cursorob.rowcount
                for row in x:
                    print(row)
                print("\n")
                ch1=input("enter your choice (A,B) :")
                if ch1=="A":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'A_sc')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="B":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'B_sc')
                    cursorob.execute(query)
                    myconn.commit()
                else:
                    print("the entered choice is not in the given option")          
            
            else:
                print("you are not eligible since required percentage is not met ")
        if ch=="3" :
            if per>=65 and per<=100:
                sid=int(input("enter ID:"))
                print (fn,"well done you have been admitted")
                print ("now choose your subjects")
                print("\n")
                cursorob=myconn.cursor()
                query="""select * from subject_comb where s_id =3;"""
                cursorob.execute(query)
                x=cursorob.fetchall()
                c=cursorob.rowcount
                for row in x:
                    print(row)
                print("\n")
                ch1=input("enter your choice (A,B,C) :")
                if ch1=="A":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'A_com')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="B":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'B_com')
                    cursorob.execute(query)
                    myconn.commit()
                elif ch1=="C":
                    cursorob=myconn.cursor()
                    query="""insert into STUDENT_INFO 
                             values ({},{},'{}','{}',{},'{}',{},'{}')""".format(sid,ch,fn,ln,age,sex,per,'C_com')
                    cursorob.execute(query)
                    myconn.commit()
                else:
                    print("the entered choice is not in the given option")
            
            else:
                print("you are not eligible since required percentage is not met ")
        print("***THANK YOU***")
    elif choice =='2':
        print ("\n")
        print(" **students info** ")
        cursor=myconn.cursor()
        query="""select *
                 from STUDENT_INFO;"""
        cursor.execute(query)
        x=cursor.fetchall()
        c=cursor.rowcount
        for row in x:
            print(row)
    elif choice == '3':
        print("Thank You for using this software...")
        break;

