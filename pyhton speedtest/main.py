# Internet Speed Tester using Python

from tkinter import *
from tkinter import messagebox
import pyspeedtest

def logic():
     st=pyspeedtest.SpeedTest("www.google.com")
     a=(str(st.download()/1048576) + "[MegaBytes per second]")
     messagebox.showinfo("Your Download speed:",a)

top=Tk()
top.title('Speed Test by Ankit, Amol and Abhay')
top.geometry('100x100')
background_label=Label(top)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

b=Button(top,text='Click to see the Internet speed',font=('San serif',20),bg='Yellow',height=1,width=30,command=logic).pack()
top.mainloop()