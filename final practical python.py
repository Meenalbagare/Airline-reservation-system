from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import time
import calendar
import datetime
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="iAmMeEnAl123",database="Airline_reservation")
cursor=conn.cursor()
cursor.execute("Select * From flight")

#Function to add flight details to the  database
def book():
    v=IntVar()
    v1=StringVar()
    no=no_entry.get()
    name=name_entry.get()
    dept=dept_entry.get()
    arr=Arr_entry.get()
    price=pr_entry.get()
    dest=des_entry.get()
    des_to=to_entry.get()
    travel=travel_entry.get()
    retur=return_entry.get()
    if(no=="" or name=="" or dept=="" or arr=="" or price=="" or dest=="" or des_to=="" or travel=="" or retur==""):
        MessageBox.showinfo("Booking status","All Fields are required")
        
        
    
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="iAmMeEnAl123",database="Airline_reservation")
        cursor=conn.cursor()
        cursor.execute("insert into flight values('"+no+"','"+name+"','"+dept+"','"+arr+"','"+price+"','"+dest+"','"+des_to+"','"+travel+"','"+retur+"')")
        cursor.execute("commit")
        no_entry.delete(0,"end")
        name_entry.delete(0,"end")
        dept_entry.delete(0,"end")
        Arr_entry.delete(0,"end")
        pr_entry.delete(0,"end")
        des_entry.delete(0,"end")
        to_entry.delete(0,"end")
        travel_entry.delete(0,"end")
        return_entry.delete(0,"end")
        MessageBox.showinfo("Booking status","Booked successfully")
        conn.close()
        
# Function to delete a flight from database
def delete():
    conn=mysql.connector.connect(host="localhost",user="root",password="iAmMeEnAl123",database="Airline_reservation")
    cursor=conn.cursor()
    cursor.execute("select Flight_no from flight")
    data=[x[0] for x in cursor.fetchall()]
    delete=no_entry.get()
    print(delete)
    if delete=="":
        MessageBox.showinfo("Information","Enter the flight number")
    elif delete not in data:
        MessageBox.showinfo("Information","Flight does not exist")
    else:
        cursor.execute("delete from flight where Flight_no={}".format(delete))
        conn.commit()
        MessageBox.showinfo("Information","Deleted succesfully")
        
# Function to modify flight details
def update():
    no=no_entry.get()
    name=name_entry.get()
    dept=dept_entry.get()
    arr=Arr_entry.get()
    price=pr_entry.get()
    dest=des_entry.get()
    des_to=to_entry.get()
    travel=travel_entry.get()
    retur=return_entry.get()
    if(no=="" or name=="" or dept=="" or arr=="" or price=="" or dest=="" or des_to=="" or travel=="" or retur==""):
        MessageBox.showinfo("Update status","All Fields are required")
    else:
        conn=mysql.connector.connect(host="localhost",user="root",password="iAmMeEnAl123",database="Airline_reservation")
        cursor=conn.cursor()
        cursor.execute("update flight set Flight_name='"+name+"',Dept_time='"+dept+"',Arrival_time='"+arr+"',Price_details='"+price+"',Destination_From='"+dest+"',Destination_To='"+des_to+"',Date_of_travel='"+travel+"',Date_of_return='"+retur+"' where Flight_no='"+no+"'")
        cursor.execute("commit")
        no_entry.delete(0,"end")
        name_entry.delete(0,"end")
        dept_entry.delete(0,"end")
        Arr_entry.delete(0,"end")
        pr_entry.delete(0,"end")
        des_entry.delete(0,"end")
        to_entry.delete(0,"end")
        travel_entry.delete(0,"end")
        return_entry.delete(0,"end")
        
        
        MessageBox.showinfo("Update status","Updated  successfully")
        conn.close()



#Functionto display all the details of all  flights
def display():
    conn=mysql.connector.connect(host="localhost",user="root",password="iAmMeEnAl123",database="Airline_reservation")
    cursor=conn.cursor()
    cursor.execute("Select * from flight")
    data=cursor.fetchall()
   
    Flight_query=Tk()
    Flight_query.configure(background="light grey")
    Flight_query.title("List all flight details")
    Flight_query.geometry("800x650")
    frm=Frame(Flight_query)
    frm.pack(anchor="center",fill=X)
    table=ttk.Treeview(frm,selectmode="browse")
    table.pack(anchor="center",pady=300)
    table["columns"]=("1","2","3","4","5","6","7","8","9")
    table["show"]="headings"
    style = ttk.Style(Flight_query)
    style.theme_use("alt")
    table.heading(1,text="Flight no")
    table.column(1,minwidth=0,width=100,anchor='c')
    table.heading(2,text="Flight name")
    table.column(2,minwidth=0,width=100,anchor='c')
    table.heading(3,text="Dept time")
    table.column(3,minwidth=0,width=100,anchor='c')
    table.heading(4,text="Arrival time")
    table.column(4,minwidth=0,width=100,anchor='c')
    table.heading(5,text="Price")
    table.column(5,minwidth=0,width=100,anchor='c')            
    table.heading(6,text="From")
    table.column(6,minwidth=0,width=100,anchor='c')
    table.heading(7,text="To")
    table.column(7,minwidth=0,width=100,anchor='c')
    table.heading(8,text="travel date")
    table.column(8,minwidth=0,width=100,anchor='c')
    table.heading(9,text="return date")
    table.column(9,minwidth=0,width=100,anchor='c')
    frm.configure(background="light grey")
    for i in data:
        table.insert('','end',values=i)

#Function to display calendar of specified year
def calendars():
    shows=Tk()
    shows.title("CALENDAR")
    shows.geometry("600x600")
    year=int(i1.get())
    see=calendar.calendar(year)
    t=Label(shows,text=see,font="Consolas 10 bold")
    t.grid(row=4,column=1,padx=15)
    shows.mainloop()

#Function to clear the screen.
def exit():
    newscreen.destroy()

#Function to clear the screen.
def exit1():
    root.destroy()

# Function to validate the fields which accept only integers         
def validate_flightno(flight_no):
    if flight_no.isdigit():
        return True
    elif flight_no is "":
        return True
    else:
        MessageBox.showinfo("information","only digits  are allowed for the flight number")
        return False

#Function to validate the fields which accept strings
def validate_passengername(name):
    if name.isalpha():
        return True
    elif name is "":
        return True
    else:
         MessageBox.showinfo("information","invalid flight name")
         return False

#Function to validate the fields which accept date as YYYY/MM/DD
def validate_travel(travel):
    date_format=travel_entry.get()
    try:
        day,month,year=map(int,date_format.split('/'))
        date=datetime.date(year,month,day)
        date_message="\nDate :"+ date_format
        
    except:
        date=0
        ValueError
        MessageBox.showinfo("information","INVALID INPUT-YOU MUST ENTER THE DATE DD/MM/YYYY")
        
#Function to validate the fields which accept date as YYYY/MM/DD
def validate_return(retur):
    date_format=return_entry.get()
    try:
        day,month,year=map(int,date_format.split('/'))
        date=datetime.date(year,month,day)
        date_message="\nDate :"+ date_format
    
    except:
        date=0
        ValueError
        MessageBox.showinfo("information","INVALID INPUT-YOU MUST ENTER THE DATE DD/MM/YYYY")
#Function to validate the fields which accept integers

        
def validate_departuretime(time):
    for i in time:
        if int(i[0])>=6:
            MessageBox.showinfo("Information","YOU MUST ENTER TIME AS HOUR<24,MIN<60 AND SEC<60")
            dept_entry.delete(0,"end")
        if int(time)>=240000:
            MessageBox.showinfo("Information","YOU MUST ENTER TIME AS HOUR<24,MIN<60 AND SEC<60")
            dept_entry.delete(0,"end")
            break   
    if time.isdigit():
        return True
    elif time is "":
        return True
    
    else:
        MessageBox.showinfo("information","invalid input")
        return False

#Function to validate the fields which accept integers
def validate_arrivaltime(times):
     if int(i[0])>=6:
        MessageBox.showinfo("Information","YOU MUST ENTER TIME AS HOUR<24,MIN<60 AND SEC<60")
        Arr_entry.delete(0,"end")
        if int(times)>=240000:
            MessageBox.showinfo("Information","YOU MUST ENTER TIME AS HOUR<24,MIN<60 AND SEC<60")
            Arr_entry.delete(0,"end")
     if times.isdigit():
         return True
     elif times is "":
         return True
    
     else:
         MessageBox.showinfo("information","invalid input")
         return False
#Function to validate the fields which accept integers
def validate_price(price):
     if price.isdigit():
        return True
     elif price is "":
        return True
     else:
        MessageBox.showinfo("information","invalid input")
        return False
#Function to validate the fields which accept strings
def validate_desplace(place):
    if place.isalpha():
        return True
    elif place is "":
        return True
    else:
         MessageBox.showinfo("information","invalid input,only characters allowed")
         return False

#Function to validate the fields which accept strings
def validate_toplace(destination):
     if destination.isalpha():
        return True
     elif destination is "":
        return True
     else:
         MessageBox.showinfo("information","invalid input,only characters allowed")
         return False

#Function to validate year in calendar
def validate_calendar(year):
    if year.isdigit():
        return True
    elif year is "":
        return True
    else:
        MessageBox.showinfo("information","Enter year in 'yyyy'")
        return False


#__main__   
name=input("Enter your name")
while name:
    root=Tk()
    root.geometry("1400x1500")
    root.configure(background="brown")
    picture=PhotoImage(file="C:\\Users\\user\\Desktop\\Computer\\Meenal\\Meenal\\Airplane-13.png")
    picture1=Label(root,image=picture)
    picture1.pack(anchor="center",fill="both",expand="true")
    root.title("AIRLINE RESERVATION SYSTEM")
    k1=Label(root,text="WELCOME TO \nAIRLINE RESERVATION SYSTEM",bg="black",fg="white",font=("Helvetica",55),relief="raised")
    k1.place(x=200,y=50)
    root.mainloop()
    break

print("PROCEED TO BOOK")




        

#__main__
#__main__
while True:
    print("KINDLY INPUT '1' TO SEE THE MENU AND TYPE IN THE REQUIRED NUMBER TO CONTINUE WITH BOOKING ")
    a=int(input("Enter 1 to see the main menu"))
    print("DISPLAYING MENU.........")
    if a==1:
        root=Tk()
        root.geometry("1500x1500+10+20")
        picture=PhotoImage(file="C:\\Users\\user\\Desktop\\Computer\\Meenal\\backg.png")
        picture1=Label(root,image=picture)
        picture1.pack(anchor="center",fill="both",expand="true")
        k1=Label(root,text="BANGALORE INTERNATIONAL AIRPORT",bg="black",fg="white",font=("Helvetica",30))
        k1.place(x=200,y=50)
        k1=Label(root,text="WELCOME TO ONLINE RESERVATION SYSTEM",bg="black",fg="white",font=("Helvetica",20))
        k1.place(x=250,y=150)
        k1=Label(root,text="1.DISPLAY THE AIRLINE RESERVATION SITE",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=250)
        k1=Label(root,text="2.DISPLAY THE GUIDELINES TO BE FOLLOWED WHILE IN THE FLIGHT",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=300)
        k1=Label(root,text="3.DISPLAY THE GUIDELINES TO BE FOLLOWED WHILE BOARDING",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=350)
        k1=Label(root,text="4.DISPLAY THE GUIDELINES TO BE FOLLOWED DURING SECURITY CHECK",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=400)
        k1=Label(root,text="5.DISPLAY THE CALENDAR FOR BOOKING",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=450)
        k1=Label(root,text="6.DISPLAY THE TRANSACTION SITE",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=500)
        k1=Label(root,text="7.EXIT",bg="black",fg="white",font=("Helvetica",15))
        k1.place(x=280,y=550)
        b2=Button(root,text="exit",font=("Arial",40,"bold"),bg="orange",command=exit1).place(x=600,y=585)
        root.mainloop()
    choice=int(input("Enter the choice"))
    if choice==0:
        print("Invalid input")
    elif choice==1:
        root=Tk()

        one=Label(root,text="AIRLINE RESERVATION",bg="red",fg="white",font=("Arial Bold",100))
        one.pack(fill=X)
        two=Label(root,text="HIGH SKY BOOKING",bg="green",fg="black",font=("Fortc Bold",100))
        two.pack(fill=X)
        three=Label(root,text="Find cheap tickets -SAVE BIG!",bg="blue",fg="white",font=("Arial Bold",54))
        three.pack(fill=X)
        four=Button(root,text=" flights\n Hotels\n Cars\n Vacations",bg="black",fg="white",font=("Arial Bold",54))
        four.pack(side=LEFT,fill=Y)
        logo=PhotoImage(file="C:\\Users\\user\\Downloads\\Screenshot (1467).png")
        labe2=Label(root,image=logo)
        labe2.pack(fill=Y,side=TOP,expand="true")
        five=Label(root,text="Comapare and book cheap flights on over 600 airlines",bg="red",fg="white",font=("Arial Bold",32))
        five.pack(side=LEFT,fill=Y)
        newlabe=Label(root,text="LOGIN FORM",font=("arial",20,"bold"),bg="black",fg="white")
        newlabe.pack(side=BOTTOM,fill=X)
        root.mainloop()


        
    elif choice==2:
         root=Tk()
         root.geometry("500x800")
         pic=Label(root,text="Guidelines to be followed strictly",fg="white",bg="red",font=("Arial Bold",56))
         pic.pack(fill=X)
         texti=Label(root,text="in the flight",fg="white",bg="red",font=("Arial Bold",56))
         texti.pack(fill=BOTH,expand="true")
         picture=PhotoImage(file="C:\\Users\\user\\Downloads\\Screenshot (1468).png")
         picture1=Label(root,image=picture)
         picture1.pack(anchor="center",fill=BOTH,expand="true")
         b2=Button(root,text="exit",font=("Arial",40,"bold"),bg="yellow",command=exit1).place(x=200,y=350)
         root.mainloop()
        
    elif choice==3:
         root=Tk()
         root.geometry("500x800")
         pic=Label(root,text="Guidelines to be followed strictly",fg="white",bg="red",font=("Arial Bold",36))
         pic.pack(fill=X)
         texti=Label(root,text="while boarding",fg="white",bg="red",font=("Arial Bold",36))
         texti.pack(fill=X)
         picture=PhotoImage(file="C:\\Users\\user\\Downloads\\Screenshot (1470).png")
         picture1=Label(root,image=picture)
         picture1.pack(fill=Y)
         b2=Button(root,text="exit",font=("Arial",40,"bold"),bg="yellow",command=exit1).place(x=215,y=350)
    
         root.mainloop()
        
    
    elif choice==4:
        root=Tk()
        root.geometry("500x800")
        pic=Label(root,text="Guidelines to be followed strictly",fg="white",bg="red",font=("Arial Bold",36))
        pic.pack(fill=X)
        texti=Label(root,text="security check-in",fg="white",bg="red",font=("Arial Bold",36))
        texti.pack(fill=X)
        picture=PhotoImage(file="C:\\Users\\user\\Downloads\\Screenshot (1472).png")
        picture1=Label(root,image=picture)
        picture1.pack(anchor="center",fill=BOTH,expand="true")
        b2=Button(root,text="exit",font=("Arial",40,"bold"),bg="yellow",command=exit1).place(x=400,y=400)
    
        root.mainloop()
        
        
    elif choice==5:
        newscreen=Tk()
        newscreen.title("calendar")
        newscreen.geometry("500x300")
        newscreen.configure(background="grey")

        t1=Label(newscreen,text="CALENDAR",font=("Arial",40,"bold"),fg="black",bg="yellow").place(x=580,y=100)
        t2=Label(newscreen,text="Enter year",font=("Arial",40,"bold"),fg="olivedrab1",bg="black").place(x=200,y=255)
        i1=Entry(newscreen,font=("Arial",40,"bold"),fg="red",width=15)
        i1.place(x=500,y=255)
        valid_year=newscreen.register(validate_calendar)
        i1.config(validate="key",validatecommand=(valid_year,'%P'))
        b1=Button(newscreen,text="check",font=("Arial",40,"bold"),bg="yellow",command=calendars).place(x=500,y=355)
        b2=Button(newscreen,text="exit",font=("Arial",40,"bold"),bg="yellow",command=exit).place(x=500,y=500)
        newscreen.mainloop()
    elif choice==6:
        root=Tk()
        root.title("TRANSACTION SITE")
        root.geometry("1500x1500+10+20")
        root.configure(background="brown")
        l1=Label(root,text="WELCOME TO THE TRANSACTION SITE OF HIGH SKY BOOKING",font=("arial",32,"bold"),bg="black",fg="white")
        l1.pack(side=TOP,fill=X)
        no=Label(root,text="Login to book in your ticket",font=("arial",34,"bold"),bg="black",fg="white")
        no.pack(side=TOP,fill=Y)
        
        l2=Label(root,text="",font=("arial",26,"bold"),bg="black",fg="white")
        l2.pack(side=BOTTOM,fill=X)

              
              
        no=Label(root,text="Flight_NO",font=("arial",13,"bold"))
        no.place(x=30,y=60)
        no_entry=ttk.Entry(root,textvariable=IntVar())
        no_entry.place(x=170,y=60)
        valid_flightno=root.register(validate_flightno)
        no_entry.config(validate="key",validatecommand=(valid_flightno,'%P'))
        
        name=Label(root,text="Flight_Name",font=("arial",13,"bold"))
        name.place(x=30,y=100)
        name_entry=ttk.Entry(root,textvariable=StringVar())
        name_entry.place(x=170,y=100)
        valid_name=root.register(validate_passengername)
        name_entry.config(validate="key",validatecommand=(valid_name,'%P'))
        
        dept=Label(root,text="Dept_time",font=("arial",13,"bold"))
        dept.place(x=30,y=140)
        dept_entry=ttk.Entry(root,textvariable=IntVar())
        dept_entry.place(x=170,y=140)
        valid_dept=root.register(validate_departuretime)
        dept_entry.config(validate="key",validatecommand=(valid_dept,'%P'))
        
        Arr=Label(root,text="Arrival_time",font=("arial",13,"bold"))
        Arr.place(x=30,y=180)
        Arr_entry=ttk.Entry(root,textvariable=IntVar())
        Arr_entry.place(x=170,y=180)
        valid_Arr=root.register(validate_arrivaltime)
        Arr_entry.config(validate="key",validatecommand=(valid_Arr,'%P'))
        
        pr=Label(root,text="price_details",font=("arial",13,"bold"))
        pr.place(x=30,y=220)
        pr_entry=ttk.Entry(root,textvariable=IntVar())
        pr_entry.place(x=170,y=220)
        valid_price=root.register(validate_price)
        pr_entry.config(validate="key",validatecommand=(valid_price,'%P'))
        
        des=Label(root,text="Destination_From",font=("arial",13,"bold"))
        des.place(x=30,y=260)
        des_entry=ttk.Entry(root,textvariable=StringVar())
        des_entry.place(x=170,y=260)
        valid_destination=root.register(validate_desplace)
        des_entry.config(validate="key",validatecommand=(valid_destination,'%P'))
        
        des_to=Label(root,text="Destination_To",font=("arial",13,"bold"))
        des_to.place(x=30,y=300)
        to_entry=ttk.Entry(root,textvariable=StringVar())
        to_entry.place(x=170,y=300)
        valid_to=root.register(validate_toplace)
        to_entry.config(validate="key",validatecommand=(valid_to,'%P'))
        
        travel=Label(root,text="Date_of_Travel",font=("arial",13,"bold"))
        travel.place(x=30,y=340)
        travel_entry=ttk.Entry(root,textvariable=StringVar())
        travel_entry.place(x=170,y=340)
        valid_trav=root.register(validate_travel)
        travel_entry.config(validate="key",validatecommand=(valid_trav,'%P'))
        
        retur=Label(root,text="Date_of_return",font=("arial",13,"bold"))
        retur.place(x=30,y=380)
        return_entry=ttk.Entry(root)
        return_entry.place(x=170,y=380)
        valid_return=root.register(validate_return)
        return_entry.config(validate="key",validatecommand=(valid_return,'%P'))
        
        book=Button(root,text="book",font=("italic",10),bg="white",command=book)
        book.place(x=30,y=420)
        delete=Button(root,text="Delete",font=("italic",10),bg="white",command=delete)
        delete.place(x=30,y=480)
        update=Button(root,text="Update",font=("italic",10),bg="white",command=update)
        update.place(x=30,y=540)
        answer=Label(root,text='')
        display=Button(root,text="display",font=("italic",10),bg="white",command=display)
        display.place(x=30,y=600)
        b2=Button(root,text="exit",font=("italic",10),bg="white",command=exit1).place(x=30,y=680)
        root.mainloop()
    elif choice==7:
        root=Tk()
        root.geometry("500x500")
        root.configure(background="brown")
        root.title("AIRLINE RESERVATION SITE")
        k1=Label(root,text="EXITING...",bg="brown",fg="white",font=("Helvetica",46))
        k1.place(x=650,y=350)
        root.mainloop()
        print("Thanks for visiting HIGH SKY BOOKING.....")
        break
    else:
        print("invalid choice")


