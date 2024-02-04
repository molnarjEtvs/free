import random
import os
os.system("cls")

class licitTermek:
    def __init__(self,nev,bid,licitLepcso):
        self.nev = nev
        self.bid = bid
        self.licitLepcso = licitLepcso
        self.licitekSzama = 0
        self.ar = 0
        self.termekMegnyerve = "NEM"

    def bidVasarlas(self,osszeg):
        self.bid += (osszeg/1000)*0.9

    def arSzamolas(self):
        self.ar = (self.bid*1000)*1.1

    def licitalas(self):
        vsz = random.randint(1,1000)
        self.licitekSzama += 1
        self.bid -= self.licitLepcso
        if vsz%12 == 0:
            self.termekMegnyerve = "Igen"
            return False
        elif self.nev.find("a")>-1 and self.nev.endswith("0") == True:
            self.bidVasarlas(random.randint(1,8))
            return True
        elif self.bid<=0:
            self.bid = 0
            return False
        else:
            return True
        
licitTermekek = []
f = open("licitTermekek.txt","r",encoding="UTF-8")
for sor in f:
    sor = sor.strip().split(";")
    nev = sor[0]
    bid = int(sor[1])
    licitLepcso = int(sor[2])
    lTermek = licitTermek(nev,bid,licitLepcso)
    licitalas = True
    while licitalas == True:
        licitalas = lTermek.licitalas()
    lTermek.arSzamolas()
    licitTermekek.append(lTermek)
f.close()


w = open("eredmenyek.txt","w",encoding="UTF-8")
for termek in licitTermekek:
    w.write(f"Név: {termek.nev}\n")
    w.write(f"Licitek száma: {termek.licitekSzama}db\n")
    w.write(f"Maradék BID: {termek.bid}\n")
    w.write(f"Ár: {termek.ar}\n")
    w.write(f"Menyerve: {termek.termekMegnyerve}\n")
    w.write("----------------------------\n")
w.close()