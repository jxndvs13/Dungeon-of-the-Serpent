import pickle
import random
import tkinter as tk
from tkinter import *
screen = Tk()
screen.geometry("703x490")
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
        self.PermHP = 0
        self.Dmg = 1
        self.Res = 0
        self.Weapon = "Normal"
        self.Spd = 1
        self.Bank = 1
        self.Symbol = "0"
    def NewMaxHP(self, n):
        o = self.MaxHP
        self.MaxHP = n
        if n != o:
            self.EditHealth(n-o)
            if P.HP == 0:
                P.HP = 1
    def EditHealth(self,n):
        self.HP += n
    def Heal(self,n):
        self.HP += n
        if self.HP > self.MaxHP:
            self.HP = self.MaxHP
    def IncHP(self,n):
        self.PermHP += n
        self.EditHealth(n)
    def NewDmg(self, n):
        self.Dmg = n
    def NewWeapon(self, x):
        self.Weapon = x
    def NewResistance(self,n):
        self.Res = n
    def NewSpeed(self, x):
        self.Spd = x
    def Hurt(self, dmg):
        ndmg = dmg - self.Res
        self.HP -= ndmg
        if self.HP < 0:
            self.HP = 0
        if self.HP < self.MaxHP/3*2+1:
            self.Symbol = "O"
        if self.HP < self.MaxHP/3+1:
            self.Symbol = "o"
        f_cord(self.x, self.y).give_stuff(self.Symbol)
    def MoveUp(self):
        global Moves
        if f_cord(self.x,self.y-1) and Moves>0:
            if f_cord(self.x, self.y - 1).CordType == " ":
                Co = f_cord(self.x, self.y)
                Co.give_stuff(" ")
                self.y -= 1
                Cn = f_cord(self.x, self.y)
                Cn.give_stuff(self.Symbol)
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
                Cn.give_stuff(self.Symbol)
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
                Cn.give_stuff(self.Symbol)
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
                Cn.give_stuff(self.Symbol)
                Moves -= 1
                RunTurn()
    def MoveSkip(self):
        global Moves
        if Moves > 0:
            Moves -= 1
            RunTurn()
    def ForceUp(self):
        Co = f_cord(self.x, self.y)
        Co.give_stuff(" ")
        self.y += -1
        Cn = f_cord(self.x, self.y)
        Cn.give_stuff(self.Symbol)
    def ForceLeft(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.x += -1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff(self.Symbol)
    def ForceDown(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.y += 1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff(self.Symbol)
    def ForceRight(self):
        Co = f_cord(P.x, P.y)
        Co.give_stuff(" ")
        self.x += 1
        Cn = f_cord(P.x, P.y)
        Cn.give_stuff(self.Symbol)
    def AttackUp(self):
        global Attacks
        Co = f_cord(P.x,P.y-1)
        if Attacks>0:
            if Co.CordType:
                if Co.CordType != " ":
                    f_enemy(P.x, P.y - 1).Hurt(self.Dmg)
                    Attacks -= 1
                elif P.Weapon == "Ranged":
                    still = "Y"
                    for r in range (2,8):
                        if f_cord(P.x,P.y-r) and still == "Y":
                            if f_cord(P.x,P.y-r).CordType != " ":
                                f_enemy(P.x,P.y-r).Hurt(self.Dmg)
                                Attacks -= 1
                                still = "N"
            if self.Weapon == "Cleave":
                C1 = f_cord(P.x+1,P.y-1)
                if C1.CordType:
                    if C1.CordType != " ":
                        f_enemy(P.x+1, P.y-1).Hurt(self.Dmg)
                        Attacks -= 1
                C2 = f_cord(P.x-1,P.y-1)
                if C2.CordType:
                    if C2.CordType != " ":
                        f_enemy(P.x-1,P.y-1).Hurt(self.Dmg)
                        Attacks -= 1
        RunTurn()
    def AttackLeft(self):
        global Attacks
        Co = f_cord(P.x - 1,P.y)
        if Attacks>0:
            if Co.CordType:
                if Co.CordType != " ":
                    f_enemy(P.x - 1, P.y).Hurt(self.Dmg)
                    Attacks -= 1
                elif P.Weapon == "Ranged":
                    still = "Y"
                    for r in range(2, 8):
                        if f_cord(P.x-r, P.y) and still == "Y":
                            if f_cord(P.x-r, P.y).CordType != " ":
                                f_enemy(P.x-r, P.y).Hurt(self.Dmg)
                                Attacks -= 1
                                still = "N"
            if self.Weapon == "Cleave":
                C1 = f_cord(P.x - 1, P.y - 1)
                if C1.CordType:
                    if C1.CordType != " ":
                        f_enemy(P.x-1, P.y - 1).Hurt(self.Dmg)
                        Attacks -= 1
                C2 = f_cord(P.x-1, P.y + 1)
                if C2.CordType:
                    if C2.CordType != " ":
                        f_enemy(P.x-1, P.y + 1).Hurt(self.Dmg)
                        Attacks -= 1
        RunTurn()
    def AttackDown(self):
        global Attacks
        Co = f_cord(P.x,P.y+1)
        if Attacks>0:
            if Co.CordType:
                if Co.CordType != " ":
                    f_enemy(P.x,P.y+1).Hurt(self.Dmg)
                    Attacks -= 1
                elif P.Weapon == "Ranged":
                    still = "Y"
                    for r in range(2, 8):
                        if f_cord(P.x, P.y+r) and still == "Y":
                            if f_cord(P.x, P.y+r).CordType != " ":
                                f_enemy(P.x, P.y+r).Hurt(self.Dmg)
                                Attacks -= 1
                                still = "N"
            if self.Weapon == "Cleave":
                C1 = f_cord(P.x+1,P.y+1)
                if C1.CordType:
                    if C1.CordType != " ":
                        f_enemy(P.x+1, P.y+1).Hurt(self.Dmg)
                        Attacks -= 1
                C2 = f_cord(P.x-1,P.y+1)
                if C2.CordType:
                    if C2.CordType != " ":
                        f_enemy(P.x-1,P.y+1).Hurt(self.Dmg)
                        Attacks -= 1
        RunTurn()
    def AttackRight(self):
        global Attacks
        Co = f_cord(P.x + 1,P.y)
        if Attacks>0:
            if Co.CordType:
                if Co.CordType != " ":
                    f_enemy(P.x + 1, P.y).Hurt(self.Dmg)
                    Attacks -= 1
                elif P.Weapon == "Ranged":
                    still = "Y"
                    for r in range(2, 8):
                        if f_cord(P.x+r, P.y) and still == "Y":
                            if f_cord(P.x+r, P.y).CordType != " ":
                                f_enemy(P.x+r, P.y).Hurt(self.Dmg)
                                Attacks -= 1
                                still = "N"
            if self.Weapon == "Cleave":
                C1 = f_cord(P.x + 1, P.y - 1)
                if C1.CordType:
                    if C1.CordType != " ":
                        f_enemy(P.x+1, P.y - 1).Hurt(self.Dmg)
                        Attacks -= 1
                C2 = f_cord(P.x + 1, P.y + 1)
                if C2.CordType:
                    if C2.CordType != " ":
                        f_enemy(P.x+1, P.y + 1).Hurt(self.Dmg)
                        Attacks -= 1
        RunTurn()
    def AttackSkip(self):
        global Attacks
        if Attacks > 0:
            Attacks -= 1
            RunTurn()
class Purchasable:
    def __init__(self,name,cost,rare,desc):
        self.Name= name
        self.Cost = cost
        self.Rarity = rare
        self.Description = desc
        global ShopC
        global ShopR
        global ShopL
        if rare==1:
            ShopC.append(self)
        elif rare==2:
            ShopR.append(self)
        elif rare==3:
            ShopL.append(self)
class Weapon(Purchasable):
    def __init__(self,name,cost,rarity,dmg,type,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.Damage = dmg
        self.Type = type
    def Equip(self):
        P.NewDmg(self.Damage)
        P.NewWeapon(self.Type)
        print("Equipped")
    def Display(self):
        return f"{self.Name}\n{self.Type}\nDmg: {self.Damage}\n{self.Description}\nCost: {self.Cost}"
class Armor(Purchasable):
    def __init__(self,name,cost,rarity,TotalHp,res,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.MaxHP = TotalHp
        self.Resistance = res
    def Equip(self):
        P.NewMaxHP(self.MaxHP+P.PermHP)
        P.NewResistance(self.Resistance)
    def Display(self):
        return f"{self.Name}\nMax HP: {self.MaxHP}\nRes: {self.Resistance}\n{self.Description}\nCost: {self.Cost}"
class Artifact(Purchasable):
    def __init__(self,name,cost,rarity,effect,spd,hp,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.Speed = spd
        self.HP = hp
        self.Text = effect
    def Equip(self):
        P.IncHP(self.HP)
        P.NewSpeed(self.Speed)
    def Display(self):
        return f"{self.Name}\n{self.Text}\n{self.Description}\nCost: {self.Cost}"
class Item(Purchasable):
    def __init__(self,name,cost,rarity,effect,hp,move,atk,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.Text = effect
        self.Heal = hp
        self.Dash = move
        self.Haste = atk
    def Equip(self):
        global Moves
        Moves += self.Dash
        global Attacks
        Attacks += self.Haste
        P.Heal(self.Heal)
    def Display(self):
        return f"{self.Name}\n{self.Text}\n{self.Description}\nCost: {self.Cost}"
class Enemy:
    def __init__(self,x,y,Smbl,Hp,Dmg,Spd,Wv,Vlu):
        self.x = x
        self.y = y
        self.Symbol = Smbl
        self.EHp = Hp
        self.EDmg = Dmg
        self.ESpd = Spd
        self.Wave = Wv
        self.Value = Vlu
        allEs.append(self)
    def nSymbol(self,sym):
        self.Symbol = sym
    def Spawn(self):
        activeEs.append(self)
        f_cord(self.x,self.y).give_stuff(self.Symbol)
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
        f_cord(self.x, self.y).give_stuff(self.Symbol)
class Thug(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"T",1,1,1,Wv,1)
    def Attack(self):
        if f_cord(self.x, self.y - 1):
            if f_cord(self.x, self.y - 1).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x - 1, self.y):
            if f_cord(self.x - 1, self.y).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x, self.y + 1):
            if f_cord(self.x, self.y + 1).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x + 1, self.y):
            if f_cord(self.x + 1, self.y).CordType == P.Symbol:
                P.Hurt(self.EDmg)
    def Hurt(self, dmg):
        self.EHp -= dmg
        if self.EHp < 1:
            activeEs.remove(self)
            Co = f_cord(self.x, self.y)
            Co.give_stuff(" ")
            P.Bank += self.Value
class Squire(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"S",2,2,1,Wv,2)
    def Attack(self):
        if f_cord(self.x, self.y - 1):
            if f_cord(self.x, self.y - 1).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x - 1, self.y):
            if f_cord(self.x - 1, self.y).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x, self.y + 1):
            if f_cord(self.x, self.y + 1).CordType == P.Symbol:
                P.Hurt(self.EDmg)
        if f_cord(self.x + 1, self.y):
            if f_cord(self.x + 1, self.y).CordType == P.Symbol:
                P.Hurt(self.EDmg)
    def Hurt(self, dmg):
        self.EHp -= dmg
        if self.EHp < 1:
            activeEs.remove(self)
            Co = f_cord(self.x, self.y)
            Co.give_stuff(" ")
            P.Bank += self.Value
        if self.EHp == 1:
            self.nSymbol("s")
            f_cord(self.x, self.y).give_stuff(self.Symbol)
def f_cord(fx, fy):
    for find in cords:
        if find.x == fx and find.y == fy:
            return find
    return None
def f_enemy(fx,fy):
    for find in activeEs:
        if find.x == fx and find.y == fy:
            return find
def WaveStart():
    global WaveN
    WaveN += 1
    for e in allEs:
        if e.Wave == WaveN:
            e.Spawn()
def RunTurn():
    global Moves
    global Attacks
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
        Moves = P.Spd
        if P.Weapon == "Light":
            Attacks = 2
        else:
            Attacks = 1
        if len(activeEs) == 0:
            WaveStart()
    PrintScreen()
def PrintScreen():
    if P.HP > 0:
        Display.config(state=NORMAL)
        Display.delete(1.0, "end-1c")
        Display.insert(tk.INSERT, f"# # # # # # # # # # #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 1).CordType} {f_cord(2, 1).CordType} {f_cord(3, 1).CordType} {f_cord(4, 1).CordType} {f_cord(5, 1).CordType} {f_cord(6, 1).CordType} {f_cord(7, 1).CordType} {f_cord(8, 1).CordType} {f_cord(9, 1).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 2).CordType} {f_cord(2, 2).CordType} {f_cord(3, 2).CordType} {f_cord(4, 2).CordType} {f_cord(5, 2).CordType} {f_cord(6, 2).CordType} {f_cord(7, 2).CordType} {f_cord(8, 2).CordType} {f_cord(9, 2).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 3).CordType} {f_cord(2, 3).CordType} {f_cord(3, 3).CordType} {f_cord(4, 3).CordType} {f_cord(5, 3).CordType} {f_cord(6, 3).CordType} {f_cord(7, 3).CordType} {f_cord(8, 3).CordType} {f_cord(9, 3).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 4).CordType} {f_cord(2, 4).CordType} {f_cord(3, 4).CordType} {f_cord(4, 4).CordType} {f_cord(5, 4).CordType} {f_cord(6, 4).CordType} {f_cord(7, 4).CordType} {f_cord(8, 4).CordType} {f_cord(9, 4).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 5).CordType} {f_cord(2, 5).CordType} {f_cord(3, 5).CordType} {f_cord(4, 5).CordType} {f_cord(5, 5).CordType} {f_cord(6, 5).CordType} {f_cord(7, 5).CordType} {f_cord(8, 5).CordType} {f_cord(9, 5).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 6).CordType} {f_cord(2, 6).CordType} {f_cord(3, 6).CordType} {f_cord(4, 6).CordType} {f_cord(5, 6).CordType} {f_cord(6, 6).CordType} {f_cord(7, 6).CordType} {f_cord(8, 6).CordType} {f_cord(9, 6).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 7).CordType} {f_cord(2, 7).CordType} {f_cord(3, 7).CordType} {f_cord(4, 7).CordType} {f_cord(5, 7).CordType} {f_cord(6, 7).CordType} {f_cord(7, 7).CordType} {f_cord(8, 7).CordType} {f_cord(9, 7).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 8).CordType} {f_cord(2, 8).CordType} {f_cord(3, 8).CordType} {f_cord(4, 8).CordType} {f_cord(5, 8).CordType} {f_cord(6, 8).CordType} {f_cord(7, 8).CordType} {f_cord(8, 8).CordType} {f_cord(9, 8).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT,
                       f"# {f_cord(1, 9).CordType} {f_cord(2, 9).CordType} {f_cord(3, 9).CordType} {f_cord(4, 9).CordType} {f_cord(5, 9).CordType} {f_cord(6, 9).CordType} {f_cord(7, 9).CordType} {f_cord(8, 9).CordType} {f_cord(9, 9).CordType} #\n", ("display_tag",))
        Display.insert(tk.INSERT, f"# # # # # # # # # # #", ("display_tag",))
        Display.config(state=DISABLED)
        Health.config(state=NORMAL)
        Health.delete(1.0, "end-1c")
        Health.insert(tk.INSERT, f"HP: {P.HP}/{P.MaxHP}")
        Health.config(state=DISABLED)
        Resistance.config(state=NORMAL)
        Resistance.delete(1.0, "end-1c")
        Resistance.insert(tk.INSERT, f"Res: {P.Res}")
        Resistance.config(state=DISABLED)
        Damage.config(state=NORMAL)
        Damage.delete(1.0, "end-1c")
        Damage.insert(tk.INSERT, f"DMG: {P.Dmg}")
        Damage.config(state=DISABLED)
        WType.config(state=NORMAL)
        WType.delete(1.0, "end-1c")
        WType.insert(tk.INSERT, f"{P.Weapon}")
        WType.config(state=DISABLED)
        Speed.config(state=NORMAL)
        Speed.delete(1.0, "end-1c")
        Speed.insert(tk.INSERT, f"SPD: {P.Spd}")
        Speed.config(state=DISABLED)
        Bank.config(state=NORMAL)
        Bank.delete(1.0, "end-1c")
        Bank.insert(tk.INSERT, f"Bank: {P.Bank}")
        Bank.config(state=DISABLED)
        ALabel.config(state=NORMAL)
        ALabel.delete(1.0, "end-1c")
        ALabel.insert(tk.INSERT, f"Attacks\n{Attacks}", ("center_tag",))
        ALabel.config(state=DISABLED)
        MLabel.config(state=NORMAL)
        MLabel.delete(1.0, "end-1c")
        MLabel.insert(tk.INSERT, f"Moves\n{Moves}", ("center_tag",))
        MLabel.config(state=DISABLED)
        WaveCounter.config(state=NORMAL)
        WaveCounter.delete(1.0, "end-1c")
        WaveCounter.insert(tk.INSERT, f"Wave {WaveN}")
        WaveCounter.config(state=DISABLED)
    else:
        Health.config(state=NORMAL)
        Health.delete(1.0, "end-1c")
        Health.insert(tk.INSERT, f"HP: {P.HP}/{P.MaxHP}")
        Health.config(state=DISABLED)
        Display.config(state=NORMAL)
        Display.delete(1.0, "end-1c")
        Display.insert(tk.INSERT, f"\n\n\n\n\n      Game Over")
        Display.config(state=DISABLED)
def RefreshShop():
    if P.Bank > 0:
        P.Bank -= 1
        global ShopC
        global ShopR
        global ShopL
        global Product1
        P1 = random.randint(0, len(ShopC) - 1)
        Product1 = ShopC[P1]
        Shop1.config(state=NORMAL)
        Shop1.delete(1.0, "end-1c")
        Shop1.insert(tk.INSERT, Product1.Display())
        Shop1.config(state=DISABLED)
        global Product2
        R2 = random.randint(1,int(WaveN + 5))
        if R2 < 6:
            P2 = random.randint(0, len(ShopC) - 1)
            Product2 = ShopC[P2]
        else:
            P2 = random.randint(0, len(ShopR) - 1)
            Product2 = ShopR[P2]
        Shop2.config(state=NORMAL)
        Shop2.delete(1.0, "end-1c")
        Shop2.insert(tk.INSERT, Product2.Display())
        Shop2.config(state=DISABLED)
        global Product3
        R3 = random.randint(1,int(WaveN * 1.2 + 3))
        if R3 < 4:
            P3 = random.randint(0, len(ShopC) - 1)
            Product3 = ShopC[P3]
        elif R3 > (WaveN + 3):
            P3 = random.randint(0, len(ShopR) - 1)
            Product3 = ShopL[P3]
        else:
            P3 = random.randint(0, len(ShopR) - 1)
            Product3 = ShopR[P3]
        Shop3.config(state=NORMAL)
        Shop3.delete(1.0, "end-1c")
        Shop3.insert(tk.INSERT, Product3.Display())
        Shop3.config(state=DISABLED)
        print(R2)
        print(R3)
def Buy1():
    if P.Bank >= Product1.Cost:
        Product1.Equip()
        P.Bank -= Product1.Cost
        PrintScreen()
def Buy2():
    if P.Bank >= Product2.Cost:
        Product2.Equip()
        P.Bank -= Product2.Cost
        PrintScreen()
def Buy3():
    if P.Bank >= Product3.Cost:
        Product3.Equip()
        P.Bank -= Product3.Cost
        PrintScreen()

with open("coordinates.dat", "rb") as cdat:
    cords = pickle.load(cdat)
P = Player()
C = f_cord(P.x,P.y)
C.give_stuff(P.Symbol)
activeEs = []
edat=open("enemies.dat","rb")
allEs=pickle.load(edat)
Cdat=open("common_loot.dat","rb")
ShopC=pickle.load(Cdat)
Rdat=open("rare_loot.dat","rb")
ShopR=pickle.load(Rdat)
Ldat=open("legendary_loot.dat","rb")
ShopL=pickle.load(Ldat)
Product1 = None
Product2 = None
Product3 = None
Moves = P.Spd
Attacks = 1
WaveN = 0
WaveStart()

Display = Text(screen,width=22,height=11,font=("fixedsys",21))
Display.place(x=10,y=10)
Display.tag_configure("display_tag", justify="center")
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
MLabel = Text(screen,width=7,height=2,font=("fixedsys",16))
MLabel.place(x=373,y=129)
MLabel.tag_configure("center_tag", justify="center")
AUp = Button(screen,width=3, height=1,font=("fixedsys",21),text="↑",command=P.AttackUp)
AUp.place(x=570,y=240)
ALeft = Button(screen,width=3, height=1,font=("fixedsys",21),text="←",command=P.AttackLeft)
ALeft.place(x=505,y=300)
ADown = Button(screen,width=3, height=1,font=("fixedsys",21),text="↓",command=P.AttackDown)
ADown.place(x=570,y=360)
ARight = Button(screen,width=3, height=1,font=("fixedsys",21),text="→",command=P.AttackRight)
ARight.place(x=635,y=300)
ASkip = Button(screen,width=6, height=3,font=("fixedsys",16),text="Skip",command=P.AttackSkip)
ASkip.place(x=570,y=299)
ALabel = Text(screen,width=7,height=2,font=("fixedsys",16))
ALabel.place(x=633,y=249)
ALabel.tag_configure("center_tag", justify="center")
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
WaveCounter = Text(screen,width=6,height=1,font=("fixedsys",21))
WaveCounter.place(x=571,y=115)
Shop1 = Text(screen,width=20,height=8,font=("fixedsys",16))
Shop1.place(x=10,y=356)
Buy1 = Button(screen,width=2,height=1,font=("fixedsys",16),text="$",command=Buy1)
Buy1.place(x=142,y=450)
Shop2 = Text(screen,width=20,height=8,font=("fixedsys",16))
Shop2.place(x=172,y=356)
Buy2 = Button(screen,width=2,height=1,font=("fixedsys",16),text="$",command=Buy2)
Buy2.place(x=304,y=450)
Shop3 = Text(screen,width=20,height=8,font=("fixedsys",16))
Shop3.place(x=334,y=356)
Buy3 = Button(screen,width=2,height=1,font=("fixedsys",16),text="$",command=Buy3)
Buy3.place(x=466,y=450)
ReShop = Button(screen,width=14,height=1,font=("fixedsys",16),text="$Refresh Shop$",command=RefreshShop)
ReShop.place(x=375,y=318)

RefreshShop()
PrintScreen()
screen.mainloop()
