import tkinter as tk
from tkinter import *

screen = Tk()
screen.geometry("750x500")
screen.resizable(False,False)

c1 = Label(text="#",width=4,height=2,font=("Arial",10))
c1.place(x=20,y=20)
c2 = Text(width=4,height=2,font=("Arial",10))
c2.place(x=55,y=20)
c3 = Text(width=4,height=2,font=("Arial",10))
c3.place(x=90,y=20)
c4 = Text(width=4,height=2,font=("Arial",10))
c4.place(x=125,y=20)
c5 = Text(width=4,height=2,font=("Arial",10))
c5.place(x=160,y=20)
c6 = Text(width=4,height=2,font=("Arial",10))
c6.place(x=195,y=20)
c7 = Text(width=4,height=2,font=("Arial",10))
c7.place(x=230,y=20)
c8 = Text(width=4,height=2,font=("Arial",10))
c8.place(x=265,y=20)
c9 = Text(width=4,height=2,font=("Arial",10))
c9.place(x=300,y=20)

def show(x):
    temp.insert(tk.INSERT,x)

Bw = Button(screen,text="↑",width=4,height=2,command=lambda:show("w"),font=("Arial",14))
Bw.place(x=600,y=330)

Ba = Button(screen,text="←",width=4,height=2,command=lambda:show("a"),font=("Arial",14))
Ba.place(x=540,y=400)

Bs = Button(screen,text="↓",width=4,height=2,command=lambda:show("s"),font=("Arial",14))
Bs.place(x=600,y=400)

Bd = Button(screen,text="→",width=4,height=2,command=lambda:show("d"),font=("Arial",14))
Bd.place(x=660,y=400)

screen.mainloop()