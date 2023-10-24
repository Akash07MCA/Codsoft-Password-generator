from tkinter import *
from random import randint

win = Tk()

def new_rand():
    passentry.delete(0,END)
    passlenght = int(myentry.get())
    mypas = ''
    for i in range(passlenght):
        mypas += chr(randint(33,126))

    passentry.insert(0,mypas)

def reset():
    myentry.delete(0,END)
    passentry.delete(0,END)

Label(win,text="PASSWORD GENERATOR....",font=("Arial",30),fg=("Red")).pack()

lf = LabelFrame(win,text="Length of password",font=("Arial",10))
lf.pack(pady=10)

myentry = Entry(lf,font=("Arial",24))
myentry.pack(pady=20,padx=20)

lab = LabelFrame(win,text="Password",font=("Arial",20))
lab.pack(pady=20)

passentry = Entry(lab, text='',font=("Arial", 24), bg="systembuttonface",border=0)
passentry.pack(pady=20,padx=20)

myframe = Frame(win)
myframe.pack(pady=20)

grbutton = Button(myframe,text="Generate password",font=("Arial",15),bg="#00ff00", command=new_rand)
grbutton.pack(pady=15)

rsbutton = Button(myframe,text="Reset",font=("Arial",20),bg="red",command=reset)
rsbutton.pack(pady=10)

win.mainloop()