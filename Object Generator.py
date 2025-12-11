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
        allEs.append(self)
class Thug(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"T",1,1,1,Wv,1)
class Squire(Enemy):
    def __init__(self,x,y,Wv):
        Enemy.__init__(self,x,y,"S",2,2,1,Wv,2)

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

#20 Characters per line. Rarities: 1=common, 2=rare, 3=legendary
#Armor and Weapon descriptions should have 3 "\n"s
arm = Armor("Chain Mail", 4, 2, 5, 1,"The protective armor\nof a soldier.\n\n")
wep = Weapon("Daggers", 2, 1, 1, "Light","Why have one blade\nwhen you could have\ntwo?\n")

#Item and Artifact descriptions should have 4 "\n"s
it = Item("Health Potion",2,1,"Restore 3 HP",3, 0, 0, "\nA bubbling red\nliquid in a small\nglass vile.\n")
art = Artifact("Winged Shoes", 7, 3, "Increase speed a lot", 3, 0,"\nI don't know who's\nwings these once\nwere, but they have\nmy pity.")

with open("enemies.dat","wb") as dat:
    pickle.dump(allEs,dat)
with open("common_loot.dat", "wb") as dat:
    pickle.dump(ShopC,dat)
with open("rare_loot.dat", "wb") as dat:
    pickle.dump(ShopR,dat)
with open("legendary_loot.dat", "wb") as dat:
    pickle.dump(ShopL,dat)