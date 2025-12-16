import pickle

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
class Armor(Purchasable):
    def __init__(self,name,cost,rarity,TotalHp,res,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.MaxHP = TotalHp
        self.Resistance = res
class Artifact(Purchasable):
    def __init__(self,name,cost,rarity,effect,spd,hp,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.Speed = spd
        self.HP = hp
        self.Text = effect
class Item(Purchasable):
    def __init__(self,name,cost,rarity,effect,hp,move,atk,desc):
        Purchasable.__init__(self,name,cost,rarity,desc)
        self.Text = effect
        self.Heal = hp
        self.Dash = move
        self.Haste = atk
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
        self.Pushed = 0
        allEs.append(self)
class Thug(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"T",1,1,1,Wv,1)
class Squire(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"S",2,2,1,Wv,2)
class Knight(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "K", 4, 3, 1, Wv, 4)
class Archer(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "A", 1, 2, 1, Wv, 3)
class Berzerker(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "B", 2, 3, 2, Wv, 3)
class Executioner(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "X", 5, 2, 1, Wv, 5)
class Rogue(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "R", 1, 2, 2, Wv, 3)
class Longbowmen(Enemy):
    def __init__(self, x, y, Wv):
        Enemy.__init__(self, x, y, "L", 3, 4, 1, Wv, 5)

allEs=[]
ShopC=[]
ShopR=[]
ShopL=[]

e = Thug(9,5,1)
e = Thug(9,1,2)
e = Thug(1,9,2)
e = Thug(1,2,3)
e = Thug(6,1,3)
e = Squire(8,9,3)
e = Archer(1,1,4
e = Thug(2,8,4)
e = Thug(1,6,4)
e = Thug(8,9,4)
e = Squire(5,1,5)
e = Thug(1,5,5)
e = Thug(9,5,5)
e = Squire(5,9,5)
e = Squire(1,1,6)
e = Squire(1,9,6)
e = Squire(9,1,6)
e = Squire(9,9,6)
e = Archer(3,1,7)
e = Archer(7,1,7)
e = Knight(9,5,7)
e = Berzerker(9,1,8)
e = Rogue(1,6,8)
e = Rogue(6,1,8)
e = Squire(5,1,9)
e = Rogue(9,1,9)
e = Squire(1,5,9)
e = Squire(9,5,9)
e = Rogue(1,9,9)
e = Squire(5,9,9)
e = Squire(3,1,10)
e = Executioner(5,5,10)
e = Squire(1,8,10)
e = Squire(9,6,10)
e = Knight(2,2,11)
e = Knight(8,2,11)
e = Knight(5,8,11)
e = Berzerker(1,1,12)
e = Berzerker(1,9,12)
e = Berzerker(9,1,12)
e = Berzerker(9,9,12)
e = (,,)
e = (,,)
e = (,,)
e = (,,)
e = (,,)
e = (,,)
e = (,,)
e = (,,)
e = (,,)

#20 Characters per line. Rarities: 1=common, 2=rare, 3=legendary
#Armor and Weapon descriptions should have 3 "\n"s
arm = Armor("Leather Armor      C", 4, 2, 5, 1,"\n\n\n")
arm = Armor("Studded Armor      C", 4, 2, 5, 1,"\n\n\n")
arm = Armor("Chain Shirt        R", 4, 2, 5, 1,"\n\n\n")
arm = Armor("Breastplate        R", 4, 2, 5, 1,"\n\n\n")
arm = Armor("Chain Mail         L", 4, 2, 5, 1,"\n\n\n")
arm = Armor("Plate Armor        L", 4, 2, 5, 1,"\n\n\n")

wep = Weapon("Daggers            C", 3, 1, 1, "Light","Why have one blade\nwhen you could have\ntwo?\n")
wep = Weapon("Longsword          C", 3, 1, 2, "Normal","\n\n\n")
wep = Weapon("Hammer             C", 2, 1, 1, "Push","\n\n\n")
wep = Weapon("Spear              C", 2, 1, 1, "Reach","\n\n\n")
wep = Weapon("Sling              C", 3, 1, 1, "Ranged","\n\n\n")
wep = Weapon("Shortbow           R", 5, 2, 2, "Ranged","\n\n\n")
wep = Weapon("Battleaxe          R", 4, 2, 2, "Cleave","\n\n\n")
wep = Weapon("Rapier             R", 4, 2, 2, "Light","\n\n\n")
wep = Weapon("Pike               R", 4, 2, 2, "Reach","\n\n\n")
wep = Weapon("Warhammer          R", 4, 2, 2, "Push","\n\n\n")
wep = Weapon("Longbow            L", 7, 3, 2, "Ranged","\n\n\n")

#Item and Artifact descriptions should have 4 "\n"s
it = Item("Health Potion      C",2,1,"Restore 3 HP",3, 0, 0, "\nA bubbling red\nliquid in a small\nglass vile.\n")
it = Item("Health Potion      R",4,2,"Restore 5 HP",5, 0, 0, "\nA bubbling red\nliquid in a small\nglass bottle.\n")
it = Item("Health Potion      L",6,3,"Restore all HP",10, 0, 0, "\nA bubbling red\nliquid in a glass\nbottle.\n")
it = Item("Dash               C",2,1,"Move again this turn",0, 1, 0, "\nSprint across the\nbattle field.\n\n")
it = Item("Dash               R",4,2,"Move two more times\nthis turn",0, 2, 0, "Sprint across the\nbattle field.\n\n")
it = Item("Dash               L",6,3,"Move three more\ntimes this turn",0, 3, 0, "Sprint across the\nbattle field.\n\n")
it = Item("Haste              C",2,1,"Attack again this turn",0, 0, 1, "\nMove with incredible\nspeed.\n\n")
it = Item("Haste              R",4,2,"Attack two more\ntimes this turn",0, 0, 1, "Move with incredible\nspeed.\n\n")
it = Item("Haste              L",6,3,"Attack three more\ntimes this turn",0, 0, 1, "Move with incredible\nspeed.\n\n")

art = Artifact("Winged Shoes       L", 7, 3, "Increase speed\nsignificantly", 3, 0,"I don't know who's\nwings these once\nwere, but they have\nmy pity.")

with open("enemies.dat","wb") as dat:
    pickle.dump(allEs,dat)
with open("common_loot.dat", "wb") as dat:
    pickle.dump(ShopC,dat)
with open("rare_loot.dat", "wb") as dat:
    pickle.dump(ShopR,dat)
with open("legendary_loot.dat", "wb") as dat:
    pickle.dump(ShopL,dat)

