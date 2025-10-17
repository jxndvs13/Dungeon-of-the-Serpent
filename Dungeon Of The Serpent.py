import pickle

class Room:
    def __init__(self):
        self.Layout =""
        self.Mcord = ""
        self.Ndoor = ""
        self.Edoor = ""
        self.Sdoor = ""
        self.Wdoor = ""
        self.NWTreasure = ""
        self.NETreasure = ""
        self.SWTreasure = ""
        self.SETreasure = ""
    def get_room_details(self):
        input("Enter layout details: ")
class Enemy:
    def __init__(self):
        self.ECord = ""
        self.Type = ""
        self.Symbol = ""
        self.EHp = ""
        self.EDmg = ""
        self.EWeapon = ""
        self.ESpd = ""
    def get_enemy_details(self):
        input("Enter the enemy type: ")
        input("Enter the symbol: ")
        input("Enter the Enemy HP: ")
        input("Enter the Enemy Damage: ")
        input("Enter the Enemy Weapon: ")
        input("Enter the Enemy Speed: ")
class Item:
    def __init__(self):
        self.Item_Name = ""
        self.Item_Cost = ""
        self.Item_Charges = ""
    def get_item_details(self):
        input("Enter the Item Name: ")
        input("Enter the Item Cost: ")
        input("Enter the Item Charges: ")
class Armor:
    def __init__(self):
        self.Armor_Name = ""
        self.Armor_Cost = ""
        self.HpUp = ""
        self.ResUp = ""
    def get_armor_details(self):
        input("Enter the Armor Name: ")
        input("Enter the Armor Cost: ")
        input("Enter the Health Increase: ")
        input("Enter the Resistance Increase: ")
class Weapon:
    def __init__(self):
        self.Weapon_Name = ""
        self.Weapon_Cost = ""
        self.Weapon_Damage = ""
        self.Weapon_Type = ""
    def get_weapon_details(self):
        input("Enter the Weapon Name: ")
        input("Enter the Weapon Cost: ")
        input("Enter the Weapon Damage: ")
        input("Enter the Weapon Type: ")
class Artifact:
    def __init__(self):
        self.Artifact_Name = ""
        self.Artifact_Cost = ""
        self.DmgUp = ""
        self.HpUp = ""
        self.SpdUp = ""
        self.ResUp = ""
    def get_artifact_details(self):
        input("Enter the Artifact Name: ")
        input("Enter the Artifact Cost: ")
        input("Enter the Damage Increase: ")
        input("Enter the Health Increase: ")
        input("Enter the Speed Increase: ")
        input("Enter the Resistance Increase: ")





