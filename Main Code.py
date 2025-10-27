import pickle
class Cord:
    def __init__(self, cid, x, y):
        self.CordID = cid
        self.x = x
        self.y = y
        self.CordType = ""
    def give_stuff(self, type):
        self.CordType = type
    def display(self):
        print(f"{self.CordID} : ({self.x},{self.y}) : {self.CordType}")
def AssignCord(find_c, all_cords):
    for find_c in all_cords:
        if find_c.cid == all_cords:
            return find_c
    return None
def PrintScreen():
    print()

#load cords
for x in range (1):
    CordDat = open("coordinates.dat", "rb")
    cords = pickle.load(CordDat)
    CordDat.close()
    for c in cords:
        fcid = AssignCord(c, cords)
