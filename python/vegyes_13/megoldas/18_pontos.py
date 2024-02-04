import os,random
os.system("cls")

class Kolcsonzes:
    def __init__(self,nev,azonosito,ido,percDij):
        self.nev = nev
        self.azonosito = azonosito
        self.ido = ido
        self.percDij = percDij
        self.fizetendo = 0
        self.sorszam = ""

    def sorszamGeneralas(self):
        return str(random.randint(300,600))

    def vegosszegSzamolas(self):
        if self.azonosito == "A" or self.azonosito == "C":
            self.fizetendo = round((self.ido*self.percDij)*0.9)
        else:
            self.fizetendo = self.ido*self.percDij

kolcsonzesek = []
f = open("kolcsonzesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip().split(",")
    nev = sor[0]
    azonosito = sor[1]
    ido = int(sor[2])
    percDij = int(sor[3])
    egyKolcsonzes = Kolcsonzes(nev,azonosito,ido,percDij)
    egyKolcsonzes.sorszam = egyKolcsonzes.sorszamGeneralas()
    egyKolcsonzes.vegosszegSzamolas()
    kolcsonzesek.append(egyKolcsonzes)
f.close()


i = open("szamlak.txt","w",encoding="utf-8")
for egy in kolcsonzesek:
    i.write(f"Név: {egy.nev}\n")
    i.write(f"Azonosító: {egy.azonosito}\n")
    i.write(f"Sorszám: #{egy.sorszam}\n")
    i.write(f"Fizetendő: {egy.ido} perc * {egy.percDij} Ft = {egy.fizetendo} Ft\n")
    i.write("----------------------------------\n")
i.close()
