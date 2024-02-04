import random

class Hitel:
    def __init__(self,nev,hitelOsszeg,thm,futamido):
       self.nev = nev
       self.hitelOsszeg = hitelOsszeg
       self.thm = thm
       self.futamido = futamido
       self.kedvezmeny = 0

    def kamatKedvezmeny(self,kedvezmeny):
        self.thm-=kedvezmeny
        self.kedvezmeny = kedvezmeny
    
    def torlesztoSzamitas(self):
        self.haviTorleszto = round(self.hitelOsszeg*(1+self.thm/100)/self.futamido)

    def ugyfelSzamKeszites(self):
        self.ugyfelszam = random.randint(11111,99999)


hitelek=[]
f = open("hitelek.htx","r",encoding="utf-8")
for sor in f:
    sor = sor.strip().split(",")
    nev = sor[0]
    hOsszeg = int(sor[1])
    thm = float(sor[2])
    futamido = int(sor[3])
    egyHitel = Hitel(nev,hOsszeg,thm,futamido)
    egyHitel.ugyfelSzamKeszites()
    egyHitel.kamatKedvezmeny(random.randint(0,2))
    egyHitel.torlesztoSzamitas()
    hitelek.append(egyHitel)
f.close()

w = open("hitelAdatok.txt","w",encoding="utf-8")
for egyAdat in hitelek:
    w.write(f"Ügyfélszám: {egyAdat.ugyfelszam}\n")
    w.write(f"Név: {egyAdat.nev}\n")
    w.write(f"Összeg: {egyAdat.hitelOsszeg} Ft\n")
    w.write(f"Futamidő: {egyAdat.futamido} hó\n")
    w.write(f"THM: {egyAdat.thm}%\n")
    w.write(f"Kamatkedvezmény: {egyAdat.kedvezmeny}%\n")
    w.write(f"Havi törlesztő: {egyAdat.haviTorleszto}Ft\n")
    w.write("++++++++++++++++++++++++++++++++++++++++\n")
w.close()