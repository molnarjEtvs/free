import random
import os
os.system("cls")
class fociCsapat:
    def __init__(self,nev,bajnokiHelyezes,edzettsegiSzint,energiaSzint):
        self.nev = nev
        self.bajnokiHelyezes = bajnokiHelyezes
        self.edzettsegiSzint = edzettsegiSzint
        self.energiaSzint = energiaSzint
        self.eredmeny = ""
        self.edzesekSzama = 0
        self.pihenesekSzama = 0


    def pihen(self):
        self.pihenesekSzama+=1
        x = random.randint(0,3)
        self.energiaSzint+=x*0.48

    def edz(self):
        x=random.randint(1,3)
        self.energiaSzint-=x*1.5
        self.edzettsegiSzint+=x*0.7
        self.edzesekSzama+=1
        if self.energiaSzint<3:
            self.pihen()
        if self.edzettsegiSzint>=9:
            return True
        else:
            return False

    

    def jatszik(self):
        dontoPont = random.randint(1000,10000)
        if self.nev.startswith("M") == True or dontoPont%13==0:
            self.bajnokiHelyezes-=2
            self.eredmeny = "NYERT"
        elif self.nev.find("a")>-1 and dontoPont%2==0:
            self.bajnokiHelyezes-=1
            self.eredmeny = "DÖNTETLEN"
        else:
            self.bajnokiHelyezes+=3
            self.eredmeny = "VESZTETT"
            

    

    


fociCsapatok = []

r = open("focicsapatok.txt","r",encoding="UTF-8")
for sor in r:
    sor = sor.strip().split("|")
    nev = sor[0]
    bh = int(sor[1])
    edsz = int(sor[2])
    ensz = float(sor[3])
    fcs = fociCsapat(nev,bh,edsz,ensz)
    edzes = False
    while edzes == False:
        edzes = fcs.edz()
    fcs.jatszik()
    fociCsapatok.append(fcs)
r.close()

w = open("fociEredmenyek.txt","w",encoding="UTF-8")
for csapat in fociCsapatok:
    w.write(f"Csapat neve: {csapat.nev}\n")
    w.write(f"Bajnoki helyezés: {csapat.bajnokiHelyezes}\n")
    w.write(f"Edzések/pihenések száma: {csapat.edzesekSzama}/{csapat.pihenesekSzama} db\n")
    w.write(f"Játék eredménye: {csapat.eredmeny}\n")
    w.write(f"Új Edzettségi Szint: {csapat.edzettsegiSzint}\n")
    w.write(f"Új Energia Szint: {csapat.energiaSzint}\n")
    w.write("*******************************\n")
w.close()