import pickle
#Generate Cords
class Cord:
    def __init__(self, id, x, y):
        self.cid = id
        self.x = x
        self.y = y
        self.CordType = ""
    def give_stuff(self, type):
        self.CordType = type
    def display(self, n):
        print(f"c{n} : ({self.x},{self.y}) : {self.CordType}")
def PrintScreen(cords):
    print(cords[c1.CordType])
cords = []
nx = 1
ny = 1

cord_generation = 1
while cord_generation == 1:
    c1 = Cord(1, nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c1.give_stuff("#")
    cords.append(c1)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c2 = Cord(2, nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c2.give_stuff("#")
    cords.append(c2)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c3 = Cord(3, nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c3.give_stuff("#")
    cords.append(c3)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c4 = Cord(4,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c4.give_stuff("#")
    cords.append(c4)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c5 = Cord(5,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c5.give_stuff("#")
    cords.append(c5)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c6 = Cord(6,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c6.give_stuff("#")
    cords.append(c6)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c7 = Cord(7,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c7.give_stuff("#")
    cords.append(c7)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c8 = Cord(8,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c8.give_stuff("#")
    cords.append(c8)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c9 = Cord(9, nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c9.give_stuff("#")
    cords.append(c9)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c10 = Cord(10,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c10.give_stuff("#")
    cords.append(c10)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c11 = Cord(11,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c11.give_stuff("#")
    cords.append(c11)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c12 = Cord(12,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c12.give_stuff("#")
    cords.append(c12)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c13 = Cord(13,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c13.give_stuff("#")
    cords.append(c13)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c14 = Cord(14,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c14.give_stuff("#")
    cords.append(c14)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c15 = Cord(15,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c15.give_stuff("#")
    cords.append(c15)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c16 = Cord(16,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c16.give_stuff("#")
    cords.append(c16)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c17 = Cord(17,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c17.give_stuff("#")
    cords.append(c17)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c18 = Cord(18, nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c18.give_stuff("#")
    cords.append(c18)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c19 = Cord(19,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c19.give_stuff("#")
    cords.append(c19)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c20 = Cord(20,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c20.give_stuff("#")
    cords.append(c20)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c21 = Cord(21,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c21.give_stuff("#")
    cords.append(c21)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c22 = Cord(22,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c22.give_stuff("#")
    cords.append(c22)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c23 = Cord(23,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c23.give_stuff("#")
    cords.append(c23)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c24 = Cord(24,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c24.give_stuff("#")
    cords.append(c24)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c25 = Cord(25,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c25.give_stuff("#")
    cords.append(c25)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c26 = Cord(26,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c26.give_stuff("#")
    cords.append(c26)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c27 = Cord(27,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c27.give_stuff("#")
    cords.append(c27)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c28 = Cord(28,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c28.give_stuff("#")
    cords.append(c28)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c29 = Cord(29,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c29.give_stuff("#")
    cords.append(c29)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c30 = Cord(30,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c30.give_stuff("#")
    cords.append(c30)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c31 = Cord(31,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c31.give_stuff("#")
    cords.append(c31)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c32 = Cord(32,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c32.give_stuff("#")
    cords.append(c32)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c33 = Cord(33,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c33.give_stuff("#")
    cords.append(c33)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c34 = Cord(34,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c34.give_stuff("#")
    cords.append(c34)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c35 = Cord(35,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c35.give_stuff("#")
    cords.append(c35)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c36 = Cord(36,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c36.give_stuff("#")
    cords.append(c36)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c37 = Cord(37,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c37.give_stuff("#")
    cords.append(c37)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c38 = Cord(38,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c38.give_stuff("#")
    cords.append(c38)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c39 = Cord(39,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c39.give_stuff("#")
    cords.append(c39)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c40 = Cord(40,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c40.give_stuff("#")
    cords.append(c40)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c41 = Cord(41,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c41.give_stuff("#")
    cords.append(c41)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c42 = Cord(42,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c42.give_stuff("#")
    cords.append(c42)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c43 = Cord(43,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c43.give_stuff("#")
    cords.append(c43)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c44 = Cord(44,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c44.give_stuff("#")
    cords.append(c44)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c45 = Cord(45,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c45.give_stuff("#")
    cords.append(c45)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c46 = Cord(46,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c46.give_stuff("#")
    cords.append(c46)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c47 = Cord(47,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c47.give_stuff("#")
    cords.append(c47)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c48 = Cord(48,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c48.give_stuff("#")
    cords.append(c48)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c49 = Cord(49,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c49.give_stuff("#")
    cords.append(c49)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c50 = Cord(50,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c50.give_stuff("#")
    cords.append(c50)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c51 = Cord(51,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c51.give_stuff("#")
    cords.append(c51)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c52 = Cord(52,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c52.give_stuff("#")
    cords.append(c52)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c53 = Cord(53,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c53.give_stuff("#")
    cords.append(c53)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c54 = Cord(54,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c54.give_stuff("#")
    cords.append(c54)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c55 = Cord(55,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c55.give_stuff("#")
    cords.append(c55)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c56 = Cord(56,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c56.give_stuff("#")
    cords.append(c56)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c57 = Cord(57,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c57.give_stuff("#")
    cords.append(c57)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c58 = Cord(58,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c58.give_stuff("#")
    cords.append(c58)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c59 = Cord(59,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c59.give_stuff("#")
    cords.append(c59)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c60 = Cord(60,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c60.give_stuff("#")
    cords.append(c60)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c61 = Cord(61,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c61.give_stuff("#")
    cords.append(c61)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c62 = Cord(62,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c62.give_stuff("#")
    cords.append(c62)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c63 = Cord(63,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c63.give_stuff("#")
    cords.append(c63)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c64 = Cord(64,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c64.give_stuff("#")
    cords.append(c64)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c65 = Cord(65,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c65.give_stuff("#")
    cords.append(c65)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c66 = Cord(66,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c66.give_stuff("#")
    cords.append(c66)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c67 = Cord(67,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c67.give_stuff("#")
    cords.append(c67)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c68 = Cord(68,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c68.give_stuff("#")
    cords.append(c68)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c69 = Cord(69,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c69.give_stuff("#")
    cords.append(c69)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c70 = Cord(70,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c70.give_stuff("#")
    cords.append(c70)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c71 = Cord(71,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c71.give_stuff("#")
    cords.append(c71)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c72 = Cord(72,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c72.give_stuff("#")
    cords.append(c72)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c73 = Cord(73,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c73.give_stuff("#")
    cords.append(c73)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c74 = Cord(74,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c74.give_stuff("#")
    cords.append(c74)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c75 = Cord(75,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c75.give_stuff("#")
    cords.append(c75)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c76 = Cord(76,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c76.give_stuff("#")
    cords.append(c76)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c77 = Cord(77,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c77.give_stuff("#")
    cords.append(c77)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c78 = Cord(78,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c78.give_stuff("#")
    cords.append(c78)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c79 = Cord(79,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c79.give_stuff("#")
    cords.append(c79)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c80 = Cord(80,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c80.give_stuff("#")
    cords.append(c80)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    c81 = Cord(81,nx, ny)
    if nx == 1 or nx == 9 or ny == 1 or ny == 9:
        c81.give_stuff("#")
    cords.append(c81)
    if nx == 9:
        nx = 1
        ny += 1
    else:
        nx += 1
    cord_generation = 0

print (cords[c1.x])