def submitsearch():
    pass

def addstudent():
    print("in addstudent")
    def submitadd():
        print("in submitadd")
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            print("in try1")
            strr = 'insert into studentdata values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            print("in try")
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} added successfully..and want to clean the form?'.format(id,name), parent=addroot)
            print("in 1")
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.askyesnocancel('Record not added due to some reason, check your data?', parent=addroot)
           
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())

        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

        print(id,name,mobile,email,address,gender,dob, addedtime, addeddate)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x480+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='#D5F5E3')
    addroot.iconbitmap('student_icon.ico')
    addroot.resizable(False,False)

    idlabel = Label(addroot,text='Enter Id: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
   
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
    activebackground='blue',activeforeground='white', command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()

def searchstudent():
    def submitsearch():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(name != ''):
                strr = 'select * from studentdata where name=%s'
                mycursor.execute(strr,(name))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END, values=vv)

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)

        elif(addeddate != ''):
            strr = 'select * from studentdata where date=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END, values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x530+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='#D5F5E3')
    searchroot.iconbitmap('student_icon.ico')
    searchroot.resizable(False,False)

    idlabel = Label(searchroot,text='Enter Id: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
   
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry= Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=420)

    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
    activebackground='blue',activeforeground='white', command=submitsearch)
    submitbtn.place(x=150,y=470)

    searchroot.mainloop()

def updatestudent():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s, mobile=%s, email=%s, address=%s, gender=%s,dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(strr,(name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} Modified Successfully..'.format(id))
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END, values=vv)
    
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x610+220+140')
    updateroot.title('Student Management System')
    updateroot.config(bg='#D5F5E3')
    updateroot.iconbitmap('student_icon.ico')
    updateroot.resizable(False,False)

    idlabel = Label(updateroot,text='Enter Id: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time: ',bg='gold2',font=('times',18,'bold'),relief=GROOVE,
    borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
   
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry= Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)

    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
    activebackground='blue',activeforeground='white', command=submitupdate)
    submitbtn.place(x=150,y=550)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    update_data = content['values']
    if (len(update_data) != 0):
        idval.set(update_data[0])
        nameval.set(update_data[1])
        mobileval.set(update_data[2])
        emailval.set(update_data[3])
        addressval.set(update_data[4])
        genderval.set(update_data[5])
        dobval.set(update_data[6])
        dateval.set(update_data[7])
        timeval.set(update_data[8])

    updateroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content =  studenttable.item(cc)
    d_id = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(d_id))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully'.format(d_id))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END, values=vv)

    print(content)

def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addedddate, addedtime = [],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]), gender.append(pp[5]), dob.append(pp[6]), addedddate.append(pp[7]), addedtime.append(pp[8])
    
    dd = ['Id', 'Name', 'Mobile', 'Email','Address','Gender','DOB0','AddedDate','AddedTime']
    df = pd.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addedddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student data saved successfully {}'.format(paths))

def exitstudent():
    result = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if (result==True):
        root.destroy()


############################################################### Database Connection
def Connectdb():
    def submitdb():
        global con,mycursor
        #host = hostval.get()
        #user = userval.get()
        #password = passwordval.get()

        host = 'localhost'
        user = 'root'
        password = 'satvik2020'

        print(host, user, password)
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect, please try again')
        try:
            strr = 'create database project1db'
            mycursor.execute(strr)
            strr = 'use project1db'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int, name varchar(20), mobile varchar(12), email varchar(30), address varchar(100), gender varchar(50),dob varchar(50),date varchar(50),time varchar(50) )'
            mycursor.execute(strr)
            messagebox.showerror('Notifications','database created and you are connected to databases ....', parent=dbroot)
            print('11')
        except:
            strr = 'use project1db'
            mycursor.execute(strr)
            messagebox.showerror('Notifications','Now you are connected to databases ....', parent=dbroot)
            print('22')

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('student_icon.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='#6ED5EB')

    idlabel = Label(dbroot,text='Enter Host: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,
    borderwidth=3,width=13,anchor='w')
    idlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text='Enter User: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,
    borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text='Enter Password: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,
    borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)
    
#################################Connection Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    
#################################Connection Button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
    activebackground='blue',activeforeground='white', command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

########################################################################### 
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%Y")
    clock.config(text='Date: '+date_string+'\n'+ 'Time: '+time_string)
    clock.after(200,tick)

################################## Intro Slider
from math import trunc
import random
colors = ['red','green','pink','yellow','blue','gold2','brown','orange']
def IntrocolorTick():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(100,IntrocolorTick)

def IntroLabelTick():
    global count,text
    if(count>=len(showtext)):
        count = 0
        text = ''
        SliderLable.config(text=text)
    else:
        text = text+showtext[count]
        SliderLable.config(text=text)
        count += 1
    SliderLable.after(200,IntroLabelTick)
#########################################################################       
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Style, Treeview
from tkinter import ttk
import pymysqlinstall 
import time
import pandas as pd

root = Tk()
root.title('Student Management System')
root.config(bg='#D5F5E3')
root.geometry('1174x700+200+50')
root.iconbitmap('student_icon.ico')
root.resizable(False,False)

########################################################################### Frames
DataEntryFrame = Frame(root,bg= '#FCF3CF', relief=GROOVE, borderwidth=5 )
DataEntryFrame.place(x=10, y=80, width=500, height=600)

################################################################ dataentry Frames
frontlabel = Label(DataEntryFrame,text='-----------Welcome-----------', width=30, font=('arial', 20 ,'italic bold'),bg='#FCF3CF')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1.Add Student',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2.Search Student',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3.Delete Student',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4.Update Student',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5.Show All',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6.Export Data',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.Exit',width=25, font=('chiller',20,'bold'),bd=6,bg='skyblue3',
activeforeground='white',relief=RIDGE,activebackground='blue',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

########################################################################### Show data frame
style = ttk.Style()
style.configure('Treeview.Heading',font=('roman',16,'bold'),background='blue',foreground = 'blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black',fieldbackground="red")

style.map('Treeview', background=[('selected', 'cyan')])

ShowDataFrame = Frame(root,bg= '#FCF3CF', relief=GROOVE, borderwidth=5 )
ShowDataFrame.place(x=550, y=80, width=615, height=600)

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = ttk.Treeview(ShowDataFrame, columns=('Id', 'Name','Mobile No','Email','Address','Gender','D.O.B','Added Date', 'Added Time'),
xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.column(column='# 1, # 2, # 3,# 4, # 5,# 6',anchor=CENTER, stretch=NO)
studenttable.column(column='# 2',anchor=CENTER, stretch=NO)
studenttable.column(column='# 3',anchor=CENTER, stretch=NO)
studenttable.column(column='# 4',anchor=CENTER, stretch=NO)
studenttable.column(column='# 5',anchor=CENTER, stretch=NO)
studenttable.column(column='# 6',anchor=CENTER, stretch=NO)
studenttable.column(column='# 7',anchor=CENTER, stretch=NO)
studenttable.column(column='# 8',anchor=CENTER, stretch=NO)

studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable.pack(fill=BOTH, expand=1)  
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)



########################################################################### Slider
showtext = 'Welcome to Student Management System'
count=0
text=''
###########################################################################
SliderLable= Label(root, text=showtext,font=('chiller',30,'italic bold'), width=35,relief=RIDGE, borderwidth=5, bg='#21E8DD')
SliderLable.place(x=260,y=10)
IntroLabelTick()
IntrocolorTick()
############################################################################ Clock
clock = Label(root,font=('times',14,'bold'),borderwidth=4, bg='lawn green',relief=RIDGE)
clock.place(x=10,y=0)
tick()

####################################################################### Connect to db
connectbutton = Button(root,text='Connect to Databse',width=20,font=('times',14,'bold'),relief=RIDGE, borderwidth=4,bg='lawn green',
activebackground='blue',activeforeground='white', command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop() 

