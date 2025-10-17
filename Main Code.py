import pickle
class Cord:
    def __init__(self, cid, x, y):
        self.CordID = cid
        self.x = x
        self.y = y
        self.Cordtype = ""
    def give_stuff(self, type):
        self.Cordtype = type


while True:
    print("")
    nid = input("Enter ID: ")
    nx = input("Enter X: ")
    ny = input("Enter Y: ")
    place = Cord(nid, nx, ny)
    doit = input("Continue? ")
    if doit == "y":
        ntype = input("Enter type: ")
        place.give_stuff(ntype)
    CordDat = open("coordinates.dat", "ab")
    pickle.dump(place, CordDat)
    CordDat.close()
#to fix: 8