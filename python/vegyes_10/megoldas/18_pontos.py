import os,random
os.system("cls")

class taxiFuvar:
    def __init__(self,azonosito,utasokSzama,kmOraAllas):
        self.azonosito = azonosito
        self.utasokSzama = utasokSzama
        self.kmOraAllas = kmOraAllas
        self.kmDij = 440
        self.szervizeles = "NEM"

    def fuvarozas(self,megtettUt):
        self.kmOraAllas += megtettUt
        self.utDij = megtettUt*self.kmDij
        
    def szamlaNyomtatas(self):
        self.szamlaSzam = random.randint(100,999)
        if self.utasokSzama>2:
            self.utDij = self.utDij*1.05

    def szervizCheck(self):
        if self.kmOraAllas>10000:
            self.szervizeles = "IGEN"

    
fuvarok = []
o = open("taxiFuvarok.txt","r",encoding="UTF-8")
for sor in o:
    sor = sor.strip().split("|")
    az = sor[0]
    utasSzam = int(sor[1])
    km = int(sor[2])
    fuvar = taxiFuvar(az,utasSzam,km)
    fuvar.fuvarozas(random.randint(10,90))
    fuvar.szamlaNyomtatas()
    fuvar.szervizCheck()
    fuvarok.append(fuvar)
o.close()

i = open("taxik.txt","w",encoding="UTF-8")
for egyFuvar in fuvarok:
    i.write(f"Azonosító: {egyFuvar.azonosito}\n")
    i.write(f"Utasok száma: {egyFuvar.utasokSzama}\n")
    i.write(f"KM állás: {egyFuvar.kmOraAllas} km\n")
    i.write(f"Számlaszám: #{egyFuvar.szamlaSzam}#\n")
    i.write(f"Útdíj: {egyFuvar.utDij} Ft\n")
    i.write(f"Szervíz szükséglet: {egyFuvar.szervizeles}\n")
    i.write("-----------------------------------------\n")
i.close()
