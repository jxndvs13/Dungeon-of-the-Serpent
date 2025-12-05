import pickle
import time
import random
import tkinter as tk
from tkinter import *
screen = Tk()
screen.geometry("720x500")
screen.resizable(False, False)

class Cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.CordType = " "
    def give_stuff(self, type):
        self.CordType = type
class Player:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.MaxHP = 3
        self.HP = 3
        self.Dmg = 1
        self.Res = 0
        self.Weapon = "Normal"
        self.Spd = 1
        self.Bank = 0
    def IncMaxHP(self, n):
        self.MaxHP += n
    def NewDmg(self, n):
        self.Dmg = n
    def NewWeapon(self, x):
        self.Weapon = X
    def Hurt(self, dmg):
        ndmg = dmg - self.Res
        self.HP -= ndmg
    def MoveUp(self):
        global Moves
        if f_cord(self.x,self.y-1) and Moves>0:
            if f_cord(self.x, self.y - 1).CordType == " ":
                Co = f_cord(self.x, self.y)
                Co.give_stuff(" ")
                self.y -= 1
                Cn = f_cord(self.x, self.y)
                Cn.give_stuff("O")
                Moves -= 1
                RunTurn()
    def MoveLeft(self):
        global Moves
        if f_cord(self.x-1,self.y) and Moves>0:
            if f_cord(self.x - 1, self.y).CordType == " ":
                Co = f_cord(P.x, P.y)
                Co.give_stuff(" ")
                self.x -= 1
                Cn = f_cord(P.x, P.y)
                Cn.give_stuff("O")
                Moves -= 1
                RunTurn()
    def MoveDown(self):
        global Moves
        if f_cord(self.x,self.y+1) and Moves>0:
            if f_cord(self.x, self.y + 1).CordType == " ":
                Co = f_cord(P.x, P.y)
                Co.give_stuff(" ")
                self.y += 1
                Cn = f_cord(P.x, P.y)
                Cn.give_stuff("O")
                Moves -= 1
                RunTurn()
    def MoveRight(self):
        global Moves
        if f_cord(self.x+1,self.y) and Moves>0:
            if f_cord(self.x + 1, self.y).CordType == " ":
                Co = f_cord(P.x, P.y)
                Co.give_stuff(" ")
                self.x += 1
                Cn = f_cord(P.x, P.y)
                Cn.give_stuff("O")
                Moves -= 1
                RunTurn()
    def MoveSkip(self):
        global Moves
        Moves -= 1
        RunTurn()
    def ForceUp(self):
        Co = f_cord(self.x, self.y)
        Co.give_stuff(" ")
        self.y += -1
        Cn = f_cord(self.x, self.y)
        Cn.give_stuff("O")
    def ForceLeft(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.x += -1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff("O")
    def ForceDown(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.y += 1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff("O")
    def ForceRight(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.x += 1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff("O")
    def AttackUp(self):
        global Attacks
        Co = f_cord(P.x,P.y + 1)
        if Co.CordType:
            if Co.CordType == "X":
                f_enemy(P.x + 1, P.y).Hurt(self.Dmg)
                Attacks -= 1
        RunTurn()
    def AttackLeft(self):
        global Attacks
        Co = f_cord(P.x - 1,P.y)
        if Co.CordType:
            if Co.CordType == "X":
                f_enemy(P.x + 1, P.y).Hurt(self.Dmg)
                Attacks -= 1
        RunTurn()
    def AttackDown(self):
        global Attacks
        Co = f_cord(P.x,P.y - 1)
        if Co.CordType == "X":
            f_enemy(P.x + 1,P.y).Hurt(self.Dmg)
        Attacks -= 1
        RunTurn()
    def AttackRight(self):
        global Attacks
        Co = f_cord(P.x + 1,P.y)
        if Co.CordType:
            if Co.CordType == "X":
                f_enemy(P.x + 1, P.y).Hurt(self.Dmg)
                Attacks -= 1
        RunTurn()
    def AttackSkip(self):
        global Attacks
        if self.Weapon == "Cleave":
            Co = f_cord(P.x, P.y-1)
            if Co.CordType:
                if Co.CordType == "X":
                    f_enemy(P.x, P.y-1).Hurt(self.Dmg)
            Co = f_cord(P.x, P.y-1)
            if Co.CordType:
                if Co.CordType == "X":
                    f_enemy(P.x , P.y-1).Hurt(self.Dmg)
            Co = f_cord(P.x - 1, P.y)
            if Co.CordType:
                if Co.CordType == "X":
                    f_enemy(P.x - 1, P.y).Hurt(self.Dmg)
            Co = f_cord(P.x + 1, P.y)
            if Co.CordType:
                if Co.CordType == "X":
                    f_enemy(P.x + 1, P.y).Hurt(self.Dmg)
        Attacks -= 1
        RunTurn()
class Weapon:
    def __init__(self):
        self.Weapon_Name = ""
        self.Weapon_Cost = ""
        self.Weapon_Damage = ""
        self.Weapon_Type = ""
    def Equip(self):
        P.NewDmg(self.Weapon_Damage)
        P.NewWeapon(self.Weapon_Type)
class Enemy:
    def __init__(self):
        self.x = 9
        self.y = 9
        self.Type = ""
        self.Symbol = "X"
        self.EHp = 1
        self.EDmg = 1
        self.EWeapon = ""
        self.ESpd = 1
        self.Wave = 1
        self.Value = 1
    def Move(self, pX, pY):
        Co = f_cord(self.x, self.y)
        CU = f_cord(self.x, self.y - 1)
        CL = f_cord(self.x - 1, self.y)
        CD = f_cord(self.x, self.y + 1)
        CR = f_cord(self.x + 1, self.y)
        if self.y>pY and self.x>pX and CU.CordType == " " and CL.CordType == " ":
            if random.randint(1,2) == 1:
                self.y -= 1
                Co.give_stuff(" ")
            else:
                self.x -= 1
                Co.give_stuff(" ")
        elif self.y<pY and self.x>pX and CD.CordType == " " and CL.CordType == " ":
            if random.randint(1,2) == 1:
                self.y += 1
                Co.give_stuff(" ")
            else:
                self.x -= 1
                Co.give_stuff(" ")
        elif self.y>pY and self.x<pX and CU.CordType == " " and CR.CordType == " ":
            if random.randint(1,2) == 1:
                self.y -= 1
                Co.give_stuff(" ")
            else:
                self.x += 1
                Co.give_stuff(" ")
        elif self.y<pY and self.x<pX and CD.CordType == " " and CR.CordType == " ":
            if random.randint(1,2) == 1:
                self.y += 1
                Co.give_stuff(" ")
            else:
                self.x += 1
                Co.give_stuff(" ")
        elif self.y > pY and CU.CordType == " ":
            self.y -= 1
            Co.give_stuff(" ")
        elif self.x > pX and CL.CordType == " ":
            self.x -= 1
            Co.give_stuff(" ")
        elif self.y < pY and CD.CordType == " ":
            self.y += 1
            Co.give_stuff(" ")
        elif self.x < pX and CR.CordType == " ":
            self.x += 1
            Co.give_stuff(" ")
        f_cord(self.x, self.y).give_stuff("X")
    def Attack(self):
        Co = f_cord(self.x, self.y)
        Co.give_stuff(" ")
        if f_cord(self.x, self.y - 1):
            if f_cord(self.x, self.y - 1).CordType == "O":
                P.Hurt(self.EDmg)
                if self.EWeapon == "Push" and f_cord(self.x, self.y - 2).CordType == " ":
                    P.ForceUp()
                if self.EWeapon == "Light":
                    P.Hurt(self.EDmg)
        if f_cord(self.x - 1, self.y):
            if f_cord(self.x - 1, self.y).CordType == "O":
                P.Hurt(self.EDmg)
                if self.EWeapon == "Push" and f_cord(self.x - 2, self.y).CordType == " ":
                    P.ForceLeft()
                if self.EWeapon == "Light":
                    P.Hurt(self.EDmg)
        if f_cord(self.x, self.y + 1):
            if f_cord(self.x, self.y + 1).CordType == "O":
                P.Hurt(self.EDmg)
                if self.EWeapon == "Push" and f_cord(self.x, self.y + 2).CordType == " ":
                    P.ForceDown()
                if self.EWeapon == "Light":
                    P.Hurt(self.EDmg)
        if f_cord(self.x+1,self.y):
            if f_cord(self.x + 1, self.y).CordType == "O":
                P.Hurt(self.EDmg)
                if self.EWeapon == "Push" and f_cord(self.x + 2, self.y).CordType == " ":
                    P.ForceRight()
                if self.EWeapon == "Light":
                    P.Hurt(self.EDmg)
        Cn = f_cord(self.x, self.y)
        Cn.give_stuff("X")
        PrintScreen()
    def Hurt(self, dmg):
        self.EHp -= dmg
        if self.EHp < 1:
            activeEs.remove(self)
            Co = f_cord(self.x, self.y)
            Co.give_stuff(" ")
            P.Bank += self.Value
def f_cord(fx, fy):
    for find in cords:
        if find.x == fx and find.y == fy:
            return find
    return None
def f_enemy(fx,fy):
    for find in activeEs:
        if find.x == fx and find.y == fy:
            return find
def RunTurn():
    global Moves
    global Attacks
    PrintScreen()
    RefreshValues()
    if Moves == 0 and Attacks == 0:
        for e in activeEs:
            if e.ESpd == 1:
                Enemy.Move(e,P.x,P.y)
            if e.ESpd == 2:
                Enemy.Move(e,P.x,P.y)
                Enemy.Move(e,P.x,P.y)
            if e.ESpd == 3:
                Enemy.Move(e,P.x,P.y)
                Enemy.Move(e,P.x,P.y)
                Enemy.Move(e,P.x,P.y)
            e.Attack()
        PrintScreen()
        RefreshValues()
        Moves = P.Spd
        if P.Weapon == "Light":
            Attacks = 2
        else:
            Attacks = 1
def PrintScreen():
    Display.config(state=NORMAL)
    Display.delete(1.0, "end-1c")
    Display.insert(tk.INSERT, f"# # # # # # # # # # #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,1).CordType} {f_cord(2,1).CordType} {f_cord(3,1).CordType} {f_cord(4,1).CordType} {f_cord(5,1).CordType} {f_cord(6,1).CordType} {f_cord(7,1).CordType} {f_cord(8,1).CordType} {f_cord(9,1).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,2).CordType} {f_cord(2,2).CordType} {f_cord(3,2).CordType} {f_cord(4,2).CordType} {f_cord(5,2).CordType} {f_cord(6,2).CordType} {f_cord(7,2).CordType} {f_cord(8,2).CordType} {f_cord(9,2).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,3).CordType} {f_cord(2,3).CordType} {f_cord(3,3).CordType} {f_cord(4,3).CordType} {f_cord(5,3).CordType} {f_cord(6,3).CordType} {f_cord(7,3).CordType} {f_cord(8,3).CordType} {f_cord(9,3).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,4).CordType} {f_cord(2,4).CordType} {f_cord(3,4).CordType} {f_cord(4,4).CordType} {f_cord(5,4).CordType} {f_cord(6,4).CordType} {f_cord(7,4).CordType} {f_cord(8,4).CordType} {f_cord(9,4).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,5).CordType} {f_cord(2,5).CordType} {f_cord(3,5).CordType} {f_cord(4,5).CordType} {f_cord(5,5).CordType} {f_cord(6,5).CordType} {f_cord(7,5).CordType} {f_cord(8,5).CordType} {f_cord(9,5).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,6).CordType} {f_cord(2,6).CordType} {f_cord(3,6).CordType} {f_cord(4,6).CordType} {f_cord(5,6).CordType} {f_cord(6,6).CordType} {f_cord(7,6).CordType} {f_cord(8,6).CordType} {f_cord(9,6).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,7).CordType} {f_cord(2,7).CordType} {f_cord(3,7).CordType} {f_cord(4,7).CordType} {f_cord(5,7).CordType} {f_cord(6,7).CordType} {f_cord(7,7).CordType} {f_cord(8,7).CordType} {f_cord(9,7).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,8).CordType} {f_cord(2,8).CordType} {f_cord(3,8).CordType} {f_cord(4,8).CordType} {f_cord(5,8).CordType} {f_cord(6,8).CordType} {f_cord(7,8).CordType} {f_cord(8,8).CordType} {f_cord(9,8).CordType} #\n")
    Display.insert(tk.INSERT,f"# {f_cord(1,9).CordType} {f_cord(2,9).CordType} {f_cord(3,9).CordType} {f_cord(4,9).CordType} {f_cord(5,9).CordType} {f_cord(6,9).CordType} {f_cord(7,9).CordType} {f_cord(8,9).CordType} {f_cord(9,9).CordType} #\n")
    Display.insert(tk.INSERT, f"# # # # # # # # # # #")
    Display.config(state=DISABLED)
def RefreshValues():

    Health.config(state=NORMAL)
    Health.delete(1.0,"end-1c")
    Health.insert(tk.INSERT, f"HP: {P.HP}/{P.MaxHP}")
    Health.config(state=DISABLED)
    Resistance.config(state=NORMAL)
    Resistance.delete(1.0,"end-1c")
    Resistance.insert(tk.INSERT, f"Res: {P.Res}")
    Resistance.config(state=DISABLED)
    Damage.config(state=NORMAL)
    Damage.delete(1.0,"end-1c")
    Damage.insert(tk.INSERT, f"DMG: {P.Dmg}")
    Damage.config(state=DISABLED)
    WType.config(state=NORMAL)
    WType.delete(1.0,"end-1c")
    WType.insert(tk.INSERT, f"{P.Weapon}")
    WType.config(state=DISABLED)
    Speed.config(state=NORMAL)
    Speed.delete(1.0,"end-1c")
    Speed.insert(tk.INSERT, f"SPD: {P.Spd}")
    Speed.config(state=DISABLED)
    Bank.config(state=NORMAL)
    Bank.delete(1.0,"end-1c")
    Bank.insert(tk.INSERT, f"Bank: {P.Bank}")
    Bank.config(state=DISABLED)

#Generate Cords
cord_generation = 1

with open("coordinates.dat", "rb") as cdat:
    cords = pickle.load(cdat)
P = Player()
C = f_cord(P.x,P.y)
C.give_stuff("O")
E = Enemy()
C = f_cord(E.x,E.y)
C.give_stuff("X")
Moves = P.Spd
Attacks = 1
activeEs = []
activeEs.append(E)

Display = Text(screen,width=21,height=11,font=("fixedsys",21))
Display.place(x=10,y=10)
MUp = Button(screen,width=3, height=1,font=("fixedsys",21),text="↑",command=P.MoveUp)
MUp.place(x=440,y=120)
MLeft = Button(screen,width=3, height=1,font=("fixedsys",21),text="←",command=P.MoveLeft)
MLeft.place(x=375,y=180)
MDown = Button(screen,width=3, height=1,font=("fixedsys",21),text="↓",command=P.MoveDown)
MDown.place(x=440,y=240)
MRight = Button(screen,width=3, height=1,font=("fixedsys",21),text="→",command=P.MoveRight)
MRight.place(x=505,y=180)
MSkip = Button(screen,width=6, height=3,font=("fixedsys",16),text="Skip",command=P.MoveSkip)
MSkip.place(x=440,y=179)
AUp = Button(screen,width=3, height=1,font=("fixedsys",21),text="↑",command=P.AttackUp)
AUp.place(x=440,y=310)
ALeft = Button(screen,width=3, height=1,font=("fixedsys",21),text="←",command=P.AttackLeft)
ALeft.place(x=375,y=370)
ADown = Button(screen,width=3, height=1,font=("fixedsys",21),text="↓",command=P.AttackDown)
ADown.place(x=440,y=430)
ARight = Button(screen,width=3, height=1,font=("fixedsys",21),text="→",command=P.AttackRight)
ARight.place(x=505,y=370)
ASkip = Button(screen,width=6, height=3,font=("fixedsys",16),text="Skip",command=P.AttackSkip)
ASkip.place(x=440,y=369)
Health = Text(screen,width=9,height=1,font=("fixedsys",21))
Health.place(x=375,y=10)
Resistance = Text(screen,width=9,height=1,font=("fixedsys",21))
Resistance.place(x=523,y=10)
Damage = Text(screen,width=9,height=1,font=("fixedsys",21))
Damage.place(x=375,y=45)
WType = Text(screen,width=9,height=1,font=("fixedsys",21))
WType.place(x=523,y=45)
Speed = Text(screen,width=9,height=1,font=("fixedsys",21))
Speed.place(x=375,y=80)
Bank = Text(screen,width=9,height=1,font=("fixedsys",21))
Bank.place(x=523,y=80)

PrintScreen()
RefreshValues()
screen.mainloop()
