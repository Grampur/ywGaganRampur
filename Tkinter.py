##from tkinter import *
##master=Tk()
##master.title('Hello World')
##l1=Label(master,text='Name').grid(row=0)
##b1=Button(master,text='Show name', command=master.quit).grid(row=1,column=0)
##e1=Entry(master)
##e1.grid(row=0,column=1)
##x=StringVar
##mainloop()



##from tkinter import *
##master=Tk()
##master.title('')
##def Printtext(event):
##    fn=e1.get()
##    ln=e2.get()
##    e1.delete(0,END)
##    e2.delete(0,END)
##    print(fn,ln)
##def Onclick ():
##    fn=e1.get()
##    ln=e2.get()
##    e1.delete(0,END)
##    e2.delete(0,END)
##    print(fn,ln)
##l1=Label(master,text='First Name')
##l2=Label(master,text='Last Name')
##e1=Entry(master)
##e2=Entry(master)
##b1=Button(master,text='Show name',command=Onclick)
##b2=Button(master,text='Quit', command=master.quit)
##l1.grid(row=0,column=0)
##l2.grid(row=1,column=0)
##e1.grid(row=2,column=0)
##e2.grid(row=3,column=0)
##b1.grid(row=4,column=0)
##b2.grid(row=5,column=0)
##b1.bind('<Return>', Printtext)
##while True:
##    master.update()
###mainloop()

from tkinter import *
master=Tk()
master.title('')
a=IntVar()
stcount=0
stpcount=0
from time import sleep
def Onclick ():
    global stcount
    a.set(e1.get())
    stcount=1
    print('hi')
def stopcountdown():
    global stpcount
    stpcount=1
l1=Label(master,textvariable=a)
e1=Entry(master)
b1=Button(master,text='Start countdown',command=Onclick)
b2=Button(master,text='Stop countdown',command=stopcountdown)
l1.grid(row=0,column=0)
e1.grid(row=1,column=0)
b1.grid(row=2,column=0)
b2.grid(row=3,column=0)
while True:
    print('Hola', stcount)
    if a.get()>0 and stcount==1:
        a.set(a.get()-1)
        print('hello')
        #sleep(1)
    if stpcount==1:
        stcount=0
        
    master.update()
    




