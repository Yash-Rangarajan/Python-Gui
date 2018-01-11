from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Inventory")

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=455, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=455, height=650, bd=8, relief="raise")
f2.pack(side=LEFT)

f3 = Frame(root, width=455, height=650, bd=8, relief="raise")
f3.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Inventory", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
submit = Label(Bottoms, font=('arial', 10, 'italic'), text="Submit", bd=0, anchor='w')
submit.grid(row=0, column=0)

#--------Column 1-----
lblRef1=Label(f1,font=('arial',16,'bold'),fg="red",text="Quantity", bd=16, justify='left')
lblRef1.grid(row=0,column=0)
lblRef2=Label(f1,font=('arial',16,'bold'),fg="red",text="Food Storage", bd=16, justify='left')
lblRef2.grid(row=0,column=1)
lblRef3=Label(f1,font=('arial',16,'bold'),fg="red",text="Expiry Date", bd=16, justify='left')
lblRef3.grid(row=0,column=2)

# --------------
txtCb1=Entry(f1,font=('arial',16,'bold'), bd=5,width=2,insertwidth=1, justify='left')
txtCb1.grid(row=1,column=0)
lblCb2=Label(f1,font=('arial',16,'bold'),text="Milk", bd=16, justify='left')
lblCb2.grid(row=1,column=1)
txtCb3=Entry(f1,font=('arial',16,'bold'), bd=5,width=8,insertwidth=1, justify='left')
txtCb3.grid(row=1,column=2)
# --------------
txtBb1=Entry(f1,font=('arial',16,'bold'), bd=5,width=2,insertwidth=1, justify='left')
txtBb1.grid(row=2,column=0)
lblBb2=Label(f1,font=('arial',16,'bold'),text="Eggs", bd=16, justify='left')
lblBb2.grid(row=2,column=1)
txtBb3=Entry(f1,font=('arial',16,'bold'), bd=5,width=8,insertwidth=1, justify='left')
txtBb3.grid(row=2,column=2)
# --------------
txtFf1=Entry(f1,font=('arial',16,'bold'), bd=5,width=2,insertwidth=1, justify='left')
txtFf1.grid(row=3,column=0)
lblFf2=Label(f1,font=('arial',16,'bold'),text="Juice", bd=16, justify='left')
lblFf2.grid(row=3,column=1)
txtFf3=Entry(f1,font=('arial',16,'bold'), bd=5,width=8,insertwidth=1, justify='left')
txtFf3.grid(row=3,column=2)
# --------------
txtSd1=Entry(f1,font=('arial',16,'bold'), bd=5,width=2,insertwidth=1, justify='left')
txtSd1.grid(row=4,column=0)
lblSd2=Label(f1,font=('arial',16,'bold'),text="Last Night's Food", bd=16, justify='left')
lblSd2.grid(row=4,column=1)
txtSd3=Entry(f1,font=('arial',16,'bold'), bd=5,width=8,insertwidth=1, justify='left')
txtSd3.grid(row=4,column=2)


#------Column 2--------
lbldate1=Label(f2,font=('arial',16,'bold'),fg="blue",text="Quantity",bd=16, justify='left')
lbldate1.grid(row=0,column=0)
lbldate2=Label(f2,font=('arial',16,'bold'),fg="blue",text="Vegetable Bin", bd=16, justify='left')
lbldate2.grid(row=0,column=1)
lbldate3=Label(f2,font=('arial',16,'bold'),fg="blue",text="Expiry Date", bd=16, justify='left')
lbldate3.grid(row=0,column=2)
# --------------
txtCcb1=Entry(f2,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCcb1.grid(row=1,column=0)
lblCcb=Label(f2,font=('arial',16,'bold'),text="Cucumber", bd=16, justify='left')
lblCcb.grid(row=1,column=1)
txtCcb2=Entry(f2,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCcb2.grid(row=1,column=2)
# --------------
txtCbb1=Entry(f2,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCbb1.grid(row=2,column=0)
lblCbb=Label(f2,font=('arial',16,'bold'),text="Tomato", bd=16, justify='left')
lblCbb.grid(row=2,column=1)
txtCbb2=Entry(f2,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCbb2.grid(row=2,column=2)
# --------------
txtCff1=Entry(f2,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCff1.grid(row=3,column=0)
lblCff=Label(f2,font=('arial',16,'bold'),text="Spinach", bd=16, justify='left')
lblCff.grid(row=3,column=1)
txtCff2=Entry(f2,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCff2.grid(row=3,column=2)
# --------------
txtCsd1=Entry(f2,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCsd1.grid(row=4,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Carrots", bd=16, justify='left')
lblCsd.grid(row=4,column=1)
txtCsd2=Entry(f2,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCsd2.grid(row=4,column=2)


#------Column 3--------
lbldte1=Label(f3,font=('arial',16,'bold'),fg="green",text="Quantity",bd=16, justify='left')
lbldte1.grid(row=0,column=0)
lbldte2=Label(f3,font=('arial',16,'bold'),fg="green",text="Freezer", bd=16, justify='left')
lbldte2.grid(row=0,column=1)
lbldte3=Label(f3,font=('arial',16,'bold'),fg="green",text="Expiry Date", bd=16, justify='left')
lbldte3.grid(row=0,column=2)
# --------------
txtCdb1=Entry(f3,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCdb1.grid(row=1,column=0)
lblCdb=Label(f3,font=('arial',16,'bold'),text="Ice-cream", bd=16, justify='left')
lblCdb.grid(row=1,column=1)
txtCdb2=Entry(f3,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCdb2.grid(row=1,column=2)
# --------------
txtCeb1=Entry(f3,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCeb1.grid(row=2,column=0)
lblCeb=Label(f3,font=('arial',16,'bold'),text="Ice cubes", bd=16, justify='left')
lblCeb.grid(row=2,column=1)
txtCeb2=Entry(f3,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCeb2.grid(row=2,column=2)
# --------------
txtCgf1=Entry(f3,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCgf1.grid(row=3,column=0)
lblCgf=Label(f3,font=('arial',16,'bold'),text="Fish", bd=16, justify='left')
lblCgf.grid(row=3,column=1)
txtCgf2=Entry(f3,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCgf2.grid(row=3,column=2)
# --------------
txtCrd1=Entry(f3,font=('arial',16,'bold'), bd=10,width=2,insertwidth=2, justify='left')
txtCrd1.grid(row=4,column=0)
lblCrd=Label(f3,font=('arial',16,'bold'),text="Chocolate", bd=16, justify='left')
lblCrd.grid(row=4,column=1)
txtCrd2=Entry(f3,font=('arial',16,'bold'), bd=10,width=8,insertwidth=2, justify='left')
txtCrd2.grid(row=4,column=2)
