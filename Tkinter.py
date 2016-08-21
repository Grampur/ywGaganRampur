from tkinter import *
master=Tk()
master.title('Hello World')
l1=Label(master,text='Name').grid(row=0)
b1=Button(master,text='Show name', command=master.quit).grid(row=1,column=0)
e1=Entry(master)
e1.grid(row=0,column=1)
x=StringVar
mainloop()
