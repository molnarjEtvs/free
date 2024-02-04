import os, random
os.system("cls")

class Suti:
    def __init__(self,nev,tipus,ar,egyseg):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar
        self.egyseg = egyseg
        self.eladas = 0
        self.bevetel = 0

    def EladasGeneralas(self):
        return random.randint(100,500)
    
    def BevetelSzamitas(self):
        self.bevetel =  self.eladas*self.ar

sutemenyek = []
o = open("suti.txt","r",encoding="utf-8")
for x in o:
    x = x.strip().split(";")
    nev = x[0]
    tipus = x[1]
    ar = int(x[2])
    egyseg = x[3]
    egySuti = Suti(nev,tipus,ar,egyseg)
    egySuti['eladas'] = egySuti.EladasGeneralas()
    egySuti.BevetelSzamitas()
    sutemenyek.append(egySuti)
o.close()


i = open("sutik.txt","w",encoding="utf-8")
for y in sutemenyek:
    i.write(f"Sütemény neve: {y.nev}\n")
    i.write(f"A sütemény kiszerelése: {y.egyseg}\n")
    i.write(f"Eladott mennyiség: {y.db} db")
    i.write(f"Bevétel: {y.bevetel} Ft\n")
    if y.bevetel>100000:
        i.write("NÉPSZERŰ\n")
    i.write("---------------------------\n")
i.close()