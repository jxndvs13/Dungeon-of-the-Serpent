import pickle
import time
import tkinter as tk
from tkinter import *
screen = Tk()
screen.geometry("720x500")
screen.resizable(False, False)

class Cord:
    def __init__(self, id, x, y):
        self.cid = id
        self.x = x
        self.y = y
        self.CordType = " "
    def give_stuff(self, type):
        self.CordType = type
class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.MaxHP = ""
        self.HP = ""
        self.Dmg = ""
        self.Res = ""
        self.Weapon = ""
        self.Spd = ""
        self.Bank = ""
    def MoveUp(self):
        Co = f_cord(self.x, self.y, cords)
        Co.give_stuff(" ")
        self.y += -1
        Cn = f_cord(self.x, self.y, cords)
        Cn.give_stuff("O")
        E.Move(self.x,self.y)
        PrintScreen()
    def MoveLeft(self):
        Co = f_cord(P.x, P.y, cords)
        Co.give_stuff(" ")
        self.x += -1
        Cn = f_cord(P.x, P.y, cords)
        Cn.give_stuff("O")
        E.Move(self.x,self.y)
        PrintScreen()
    def MoveDown(self):
        Co = f_cord(P.x, P.y, cords)
        Co.give_stuff(" ")
        self.y += 1
        Cn = f_cord(P.x, P.y, cords)
        Cn.give_stuff("O")
        E.Move(self.x,self.y)
        PrintScreen()
    def MoveRight(self):
        Co = f_cord(P.x, P.y, cords)
        Co.give_stuff(" ")
        self.x += 1
        Cn = f_cord(P.x, P.y, cords)
        Cn.give_stuff("O")
        E.Move(self.x,self.y)
        PrintScreen()
class Enemy:
    def __init__(self):
        self.x = 9
        self.y = 9
        self.Type = ""
        self.Symbol = ""
        self.EHp = ""
        self.EDmg = ""
        self.EWeapon = ""
        self.ESpd = ""
    def Move(self, pX, pY):
        global cords
        Co = f_cord(self.x, self.y, cords)
        Co.give_stuff(" ")
        CU = f_cord(self.x, self.y - 1, cords)
        CL = f_cord(self.x - 1, self.y, cords)
        CD = f_cord(self.x, self.y + 1, cords)
        CR = f_cord(self.x + 1, self.y, cords)
        if self.y > pY and CU.CordType == " ":
            self.y -= 1
        elif self.x > pX and CL.CordType == " ":
            self.x -= 1
        elif self.y < pY and CD.CordType == " ":
            self.y += 1
        elif self.x < pX and CR.CordType == " ":
            self.x += 1
        Cn = f_cord(self.x, self.y, cords)
        Cn.give_stuff("X")
        PrintScreen()

def f_cord(fx, fy, all_cords):
    for find in all_cords:
        if find.x == fx and find.y == fy:
            return find
    return None
def PrintScreen():
    Display.config(state=NORMAL)
    Display.delete(1.0, "end-1c")
    Display.insert(tk.INSERT, f"# # # # # # # # # # #\n")
    Display.insert(tk.INSERT,f"# {c1.CordType} {c2.CordType} {c3.CordType} {c4.CordType} {c5.CordType} {c6.CordType} {c7.CordType} {c8.CordType} {c9.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c10.CordType} {c11.CordType} {c12.CordType} {c13.CordType} {c14.CordType} {c15.CordType} {c16.CordType} {c17.CordType} {c18.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c19.CordType} {c20.CordType} {c21.CordType} {c22.CordType} {c23.CordType} {c24.CordType} {c25.CordType} {c26.CordType} {c27.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c28.CordType} {c29.CordType} {c30.CordType} {c31.CordType} {c32.CordType} {c33.CordType} {c34.CordType} {c35.CordType} {c36.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c37.CordType} {c38.CordType} {c39.CordType} {c40.CordType} {c41.CordType} {c42.CordType} {c43.CordType} {c44.CordType} {c45.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c46.CordType} {c47.CordType} {c48.CordType} {c49.CordType} {c50.CordType} {c51.CordType} {c52.CordType} {c53.CordType} {c54.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c55.CordType} {c56.CordType} {c57.CordType} {c58.CordType} {c59.CordType} {c60.CordType} {c61.CordType} {c62.CordType} {c63.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c64.CordType} {c65.CordType} {c66.CordType} {c67.CordType} {c68.CordType} {c69.CordType} {c70.CordType} {c71.CordType} {c72.CordType} #\n")
    Display.insert(tk.INSERT,f"# {c73.CordType} {c74.CordType} {c75.CordType} {c76.CordType} {c77.CordType} {c78.CordType} {c79.CordType} {c80.CordType} {c81.CordType} #\n")
    Display.insert(tk.INSERT, f"# # # # # # # # # # #")
    Display.config(state=DISABLED)
cords = []
nx = 1
ny = 1

#Generate Cords
cord_generation = 1
while cord_generation == 1:
    c1 = Cord(1, nx, ny)
    cords.append(c1)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c2 = Cord(2, nx, ny)
    cords.append(c2)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c3 = Cord(3, nx, ny)
    cords.append(c3)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c4 = Cord(4,nx, ny)
    cords.append(c4)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c5 = Cord(5,nx, ny)
    cords.append(c5)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c6 = Cord(6,nx, ny)
    cords.append(c6)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c7 = Cord(7,nx, ny)
    cords.append(c7)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c8 = Cord(8,nx, ny)
    cords.append(c8)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c9 = Cord(9, nx, ny)
    cords.append(c9)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c10 = Cord(10,nx, ny)
    cords.append(c10)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c11 = Cord(11,nx, ny)
    cords.append(c11)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c12 = Cord(12,nx, ny)
    cords.append(c12)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c13 = Cord(13,nx, ny)
    cords.append(c13)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c14 = Cord(14,nx, ny)
    cords.append(c14)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c15 = Cord(15,nx, ny)
    cords.append(c15)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c16 = Cord(16,nx, ny)
    cords.append(c16)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c17 = Cord(17,nx, ny)
    cords.append(c17)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c18 = Cord(18, nx, ny)
    cords.append(c18)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c19 = Cord(19,nx, ny)
    cords.append(c19)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c20 = Cord(20,nx, ny)
    cords.append(c20)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c21 = Cord(21,nx, ny)
    cords.append(c21)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c22 = Cord(22,nx, ny)
    cords.append(c22)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c23 = Cord(23,nx, ny)
    cords.append(c23)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c24 = Cord(24,nx, ny)
    cords.append(c24)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c25 = Cord(25,nx, ny)
    cords.append(c25)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c26 = Cord(26,nx, ny)
    cords.append(c26)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c27 = Cord(27,nx, ny)
    cords.append(c27)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c28 = Cord(28,nx, ny)
    cords.append(c28)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c29 = Cord(29,nx, ny)
    cords.append(c29)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c30 = Cord(30,nx, ny)
    cords.append(c30)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c31 = Cord(31,nx, ny)
    cords.append(c31)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c32 = Cord(32,nx, ny)
    cords.append(c32)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c33 = Cord(33,nx, ny)
    cords.append(c33)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c34 = Cord(34,nx, ny)
    cords.append(c34)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c35 = Cord(35,nx, ny)
    cords.append(c35)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c36 = Cord(36,nx, ny)
    cords.append(c36)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c37 = Cord(37,nx, ny)
    cords.append(c37)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c38 = Cord(38,nx, ny)
    cords.append(c38)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c39 = Cord(39,nx, ny)
    cords.append(c39)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c40 = Cord(40,nx, ny)
    cords.append(c40)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c41 = Cord(41,nx, ny)
    cords.append(c41)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c42 = Cord(42,nx, ny)
    cords.append(c42)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c43 = Cord(43,nx, ny)
    cords.append(c43)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c44 = Cord(44,nx, ny)
    cords.append(c44)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c45 = Cord(45,nx, ny)
    cords.append(c45)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c46 = Cord(46,nx, ny)
    cords.append(c46)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c47 = Cord(47,nx, ny)
    cords.append(c47)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c48 = Cord(48,nx, ny)
    cords.append(c48)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c49 = Cord(49,nx, ny)
    cords.append(c49)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c50 = Cord(50,nx, ny)
    cords.append(c50)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c51 = Cord(51,nx, ny)
    cords.append(c51)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c52 = Cord(52,nx, ny)
    cords.append(c52)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c53 = Cord(53,nx, ny)
    cords.append(c53)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c54 = Cord(54,nx, ny)
    cords.append(c54)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c55 = Cord(55,nx, ny)
    cords.append(c55)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c56 = Cord(56,nx, ny)
    cords.append(c56)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c57 = Cord(57,nx, ny)
    cords.append(c57)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c58 = Cord(58,nx, ny)
    cords.append(c58)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c59 = Cord(59,nx, ny)
    cords.append(c59)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c60 = Cord(60,nx, ny)
    cords.append(c60)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c61 = Cord(61,nx, ny)
    cords.append(c61)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c62 = Cord(62,nx, ny)
    cords.append(c62)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c63 = Cord(63,nx, ny)
    cords.append(c63)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c64 = Cord(64,nx, ny)
    cords.append(c64)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c65 = Cord(65,nx, ny)
    cords.append(c65)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c66 = Cord(66,nx, ny)
    cords.append(c66)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c67 = Cord(67,nx, ny)
    cords.append(c67)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c68 = Cord(68,nx, ny)
    cords.append(c68)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c69 = Cord(69,nx, ny)
    cords.append(c69)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c70 = Cord(70,nx, ny)
    cords.append(c70)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c71 = Cord(71,nx, ny)
    cords.append(c71)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c72 = Cord(72,nx, ny)
    cords.append(c72)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c73 = Cord(73,nx, ny)
    cords.append(c73)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c74 = Cord(74,nx, ny)
    cords.append(c74)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c75 = Cord(75,nx, ny)
    cords.append(c75)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c76 = Cord(76,nx, ny)
    cords.append(c76)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c77 = Cord(77,nx, ny)
    cords.append(c77)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c78 = Cord(78,nx, ny)
    cords.append(c78)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c79 = Cord(79,nx, ny)
    cords.append(c79)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c80 = Cord(80,nx, ny)
    cords.append(c80)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c81 = Cord(81,nx, ny)
    cords.append(c81)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    cord_generation = 0

P = Player()
C = f_cord(P.x,P.y,cords)
C.give_stuff("O")
E = Enemy()
C = f_cord(E.x,E.y,cords)
C.give_stuff("X")

Display = Text(screen,width=21,height=11,font=("fixedsys",21))
Display.place(x=10,y=10)
MUp = Button(screen,width=3, height=1,font=("fixedsys",21),text="↑",command=P.MoveUp)
MUp.place(x=75,y=360)
MLeft = Button(screen,width=3, height=1,font=("fixedsys",21),text="←",command=P.MoveLeft)
MLeft.place(x=10,y=420)
MDown = Button(screen,width=3, height=1,font=("fixedsys",21),text="↓",command=P.MoveDown)
MDown.place(x=75,y=420)
MRight = Button(screen,width=3, height=1,font=("fixedsys",21),text="→",command=P.MoveRight)
MRight.place(x=140,y=420)

PrintScreen()
screen.mainloop()
