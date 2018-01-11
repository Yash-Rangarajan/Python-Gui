from tkinter import *
import random
import time
import datetime
import numbers
from tkinter import messagebox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Recipe")

Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, relief="raise")
Bottoms.pack(side=BOTTOM)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=180, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=500, bd=8, relief="sunken")
f2a.pack(side=BOTTOM)



f2 = Frame(root, width=440, height=650, bd=8, relief="sunken")
f2.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Recipe Suggestions", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

#------Column 1a--------
lb1=Label(f1a,font=('arial',16,'bold'),text="In  a bowl, combine flour, cocoa, sugar, vanilla essence and melted butter.",bd=16, justify='left')
lb1.grid(row=0,column=0)
adc=Label(f1a,font=('arial',16,'bold'),text="Add eggs and mix together. Pour into a lined tin and bake for",bd=16, justify='left')
adc.grid(row=1,column=0)
lb12=Label(f1a,font=('arial',16,'bold'),text="25-35 minutes.If cake springs back,its cooked. Icing: Mix together icing",bd=16, justify='left')
lb12.grid(row=2,column=0)
lb13=Label(f1a,font=('arial',16,'bold'),text="sugar, cocoa, milk and butter. Ice cake once cooled.",bd=16, justify='left')
lb13.grid(row=3,column=0)

#------Column 1b--------
lblde1=Label(f2a,font=('arial',16,'bold'),fg="red",text="Ingredients",bd=16, justify='left')
lblde1.grid(row=0,column=0)
lblde2=Label(f2a,font=('arial',16,'bold'),fg="red",text="Servings", bd=16, justify='left')
lblde2.grid(row=0,column=1)
lblde3=Label(f2a,font=('arial',16,'bold'),fg="red",text="Ingredients",bd=16, justify='left')
lblde3.grid(row=0,column=2)
lblde4=Label(f2a,font=('arial',16,'bold'),fg="red",text="Servings", bd=16, justify='left')
lblde4.grid(row=0,column=3)
# --------------
lblCkb0=Label(f2a,font=('arial',16,'bold'),text="Self Raising Flour", bd=16, justify='left')
lblCkb0.grid(row=1,column=0)
lblCkb1=Label(f2a,font=('arial',16,'bold'),text="1 cup", bd=16, justify='left')
lblCkb1.grid(row=1,column=1)
lblCkb2=Label(f2a,font=('arial',16,'bold'),text="Cocoa Powder", bd=16, justify='left')
lblCkb2.grid(row=1,column=2)
lblCkb3=Label(f2a,font=('arial',16,'bold'),text="3 tbsp", bd=16, justify='left')
lblCkb3.grid(row=1,column=3)

# --------------
txtCdb1=Label(f2a,font=('arial',16,'bold'), bd=10,text="Butter" , justify='left')
txtCdb1.grid(row=2,column=0)
lblCdb=Label(f2a,font=('arial',16,'bold'),text="250 gms", bd=16, justify='left')
lblCdb.grid(row=2,column=1)
txtCdb2=Label(f2a,font=('arial',16,'bold'), bd=10,text="Caster Sugar" , justify='left')
txtCdb2.grid(row=2,column=2)
lblCdb3=Label(f2a,font=('arial',16,'bold'),text="1/2 cup", bd=16, justify='left')
lblCdb3.grid(row=2,column=3)

# --------------
txtCjf1=Label(f2a,font=('arial',16,'bold'),text="Vanilla Essence", bd=10, justify='left')
txtCjf1.grid(row=3,column=0)
lblCjf=Label(f2a,font=('arial',16,'bold'),text="1 tsp", bd=16, justify='left')
lblCjf.grid(row=3,column=1)
txtCjf1=Label(f2a,font=('arial',16,'bold'),text="Eggs", bd=10, justify='left')
txtCjf1.grid(row=3,column=2)
lblCjf=Label(f2a,font=('arial',16,'bold'),text="2", bd=16, justify='left')
lblCjf.grid(row=3,column=3)

# --------------
txtCnd1=Label(f2a,font=('arial',16,'bold'),text="Sifted Icing Sugar", bd=10, justify='left')
txtCnd1.grid(row=4,column=0)
lblCnd=Label(f2a,font=('arial',16,'bold'),text="1 cup", bd=16, justify='left')
lblCnd.grid(row=4,column=1)
txtCnd1=Label(f2a,font=('arial',16,'bold'),text="Cocoa Powder", bd=10, justify='left')
txtCnd1.grid(row=4,column=2)
lblCnd=Label(f2a,font=('arial',16,'bold'),text="1 tsp", bd=16, justify='left')
lblCnd.grid(row=4,column=3)





#------Column 2--------
lbldate1=Label(f2,font=('arial',16,'bold'),fg="red",text="Serial No",bd=16, justify='left')
lbldate1.grid(row=0,column=0)
lbldate2=Label(f2,font=('arial',16,'bold'),fg="red",text="Recipe", bd=16, justify='left')
lbldate2.grid(row=0,column=1)

# --------------
lblCcb0=Label(f2,font=('arial',16,'bold'),text="1", bd=16, justify='left')
lblCcb0.grid(row=1,column=0)
lblCcb=Label(f2,font=('arial',16,'bold'),text="Aloo Paratha", bd=16, justify='left')
lblCcb.grid(row=1,column=1)

# --------------
txtCbb1=Label(f2,font=('arial',16,'bold'), bd=10,width=2,text="2" , justify='left')
txtCbb1.grid(row=2,column=0)
lblCbb=Label(f2,font=('arial',16,'bold'),text="Shahi Paneer", bd=16, justify='left')
lblCbb.grid(row=2,column=1)

# --------------
txtCff1=Label(f2,font=('arial',16,'bold'),text="3", bd=10,width=2, justify='left')
txtCff1.grid(row=3,column=0)
lblCff=Label(f2,font=('arial',16,'bold'),text="Chana Masala", bd=16, justify='left')
lblCff.grid(row=3,column=1)

# --------------
txtCsd1=Label(f2,font=('arial',16,'bold'),text="4", bd=10,width=2, justify='left')
txtCsd1.grid(row=4,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Rajma Chawal", bd=16, justify='left')
lblCsd.grid(row=4,column=1)

# --------------
txtCsd1=Label(f2,font=('arial',16,'bold'),text="5", bd=10,width=2, justify='left')
txtCsd1.grid(row=5,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Chana Bhatura", bd=16, justify='left')
lblCsd.grid(row=5,column=1)

# --------------
txtCsd1=Label(f2,font=('arial',16,'bold'),text="6", bd=10,width=2, justify='left')
txtCsd1.grid(row=6,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Gulab Jamun", bd=16, justify='left')
lblCsd.grid(row=6,column=1)

# --------------
txtCsd1=Label(f2,font=('arial',16,'bold'),text="7",relief="raise", bd=10,width=2, justify='left')
txtCsd1.grid(row=7,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Chocolate cake",relief="raise", bd=16, justify='left')
lblCsd.grid(row=7,column=1)

# --------------
txtCsd1=Label(f2,font=('arial',16,'bold'),text="8", bd=10,width=2, justify='left')
txtCsd1.grid(row=8,column=0)
lblCsd=Label(f2,font=('arial',16,'bold'),text="Rasmalai", bd=16, justify='left')
lblCsd.grid(row=8,column=1)


