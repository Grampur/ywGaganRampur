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

##from tkinter import *
##master=Tk()
##master.title('')
##a=IntVar()
##stcount=0
##stpcount=0
##from time import sleep
##def Onclick ():
##    global stcount
##    global stpcount
##    if stpcount==0:
##        a.set(e1.get())
##    stcount=1
##    stpcount=0
##def stopcountdown():
##    global stpcount
##    global stcount
##    stcount=0
##    stpcount=1
##l1=Label(master,textvariable=a)
##e1=Entry(master)
##b1=Button(master,text='Start countdown',command=Onclick)
##b2=Button(master,text='Stop countdown',command=stopcountdown)
##l1.grid(row=0,column=0)
##e1.grid(row=1,column=0)
##b1.grid(row=2,column=0)
##b2.grid(row=3,column=0)
##while True:
##    if a.get()>0 and stcount==1:
##        a.set(a.get()-1)
##    if stpcount==1:
##        stcount=0
##    master.update()

from tkinter import *
master=Tk()
master.title('Calculator')
a=IntVar()
def b11 ():
    a.set(1)
    
l1=Label(master,textvariable=a)
b1=Button(master,text='1',width=2,command=b11)
b2=Button(master,text='2',width=2)   
b3=Button(master,text='3',width=2)
b4=Button(master,text='4',width=2)
b5=Button(master,text='5',width=2)
b6=Button(master,text='6',width=2)
b7=Button(master,text='7',width=2)
b8=Button(master,text='8',width=2)
b9=Button(master,text='9',width=2)
b0=Button(master,text='0',width=2)
badd=Button(master,text='+',width=2)
bminus=Button(master,text='-',width=2)
bmultiply=Button(master,text='*',width=2)
bdivide=Button(master,text='/',width=2)
bequal=Button(master,text='=',width=2)
bclear=Button(master,text='C',width=2)
b9.grid(row=2,column=2,padx=5,pady=5)
b8.grid(row=2,column=1,padx=5,pady=5)
b7.grid(row=2,column=0,padx=5,pady=5)
b6.grid(row=3,column=2,padx=5,pady=5)
b5.grid(row=3,column=1,padx=5,pady=5)
b4.grid(row=3,column=0,padx=5,pady=5)
b3.grid(row=4,column=2,padx=5,pady=5)
b2.grid(row=4,column=1,padx=5,pady=5)
b1.grid(row=4,column=0,padx=5,pady=5)
b0.grid(row=5,column=1,padx=5,pady=5)
badd.grid(row=4,column=3,padx=5,pady=5)
bminus.grid(row=3,column=3,padx=5,pady=5)
bmultiply.grid(row=5,column=0,padx=5,pady=5)
bdivide.grid(row=5,column=2,padx=5,pady=5)
bequal.grid(row=5,column=3,padx=5,pady=5)
bclear.grid(row=2,column=3,padx=5,pady=5)
l1.grid(row=1,column=0,columnspan=2)
