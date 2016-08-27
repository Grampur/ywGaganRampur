##from tkinter import *
##master=Tk()
##master.title('Hello World')
##l1=Label(master,text='Name').grid(row=0)
##b1=Button(master,text='Show name', command=master.quit).grid(row=1,column=0)
##e1=Entry(master)
##e1.grid(row=0,column=1)
##x=StringVar
##mainloop()



from tkinter import *
master=Tk()
master.title('')
def Printtext(event):
    fn=e1.get()
    ln=e2.get()
    e1.delete(0,END)
    e2.delete(0,END)
    print(fn,ln)
def Onclick ():
    fn=e1.get()
    ln=e2.get()
    e1.delete(0,END)
    e2.delete(0,END)
    print(fn,ln)
l1=Label(master,text='first Name')
l2=Label(master,text='last Name')
e1=Entry(master)
e2=Entry(master)
b1=Button(master,text='Show name',command=Onclick)
b2=Button(master,text='Quit', command=master.quit)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=2,column=0)
e2.grid(row=3,column=0)
b1.grid(row=4,column=0)
b2.grid(row=5,column=0)
b1.bind('<Return>', Printtext)
while True:
    master.update()
#mainloop()
