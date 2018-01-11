import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time

conn=sqlite3.connect("login.db")
curs=conn.cursor()
root=Tk()


root.title("Login form")
text1=Label(root, text="User Name", fg="red")
text2=Label(root, text="Password", fg="blue")

#prepare the inputs to be taken
userinp1=Entry(root)
userinp2=Entry(root,show="*")

#grid layout placement

text1.grid(row= 0)
text2.grid(row=1, column=0)

userinp1.grid(row=0,column=1)
userinp2.grid(row=1, column=1)








gmt = time.localtime(time.time())
fmt = '%a, %d %b %Y %H:%M:%S IST'
str = time.strftime(fmt, gmt)
hdr = 'Date: ' + str
print (hdr)       
Label(text=hdr, width=10).grid(row=7)



def create_table():
     c=userinp1.get()
     d=userinp2.get()
     curs.execute("create table if not exists DATA(username TEXT, password TEXT)")
     curs.execute("INSERT INTO DATA VALUES(?,?)",(c,d))
     conn.commit()
     print(c)
     print(d)

#def entry():
    #curs.execute("SELECT * FROM DATA")
    #data=curs.fetchall()
    #print(data)

#submit button
button1= Button(root, text="Submit", command= create_table , bg = "grey")
button1.grid(row=3,column=0)
button2= Button(root, text="Exit", command=root.destroy , bg = "grey")
button2.grid(row=3,column=1)

#entry()
root.mainloop()
