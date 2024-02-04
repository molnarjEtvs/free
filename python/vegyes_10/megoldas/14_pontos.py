import os
os.system("cls")


def taxiAzonositokRogzitese():
    azonositok = []
    while True:
        azonosito = input("Add meg a TAXI azonosítóját: ")
        if azonosito != "":
            azonositok.append(azonosito.upper())
        else:
            return azonositok
        

def taxiElemzes(azonositok):
    szervizekSzama = 0 #ha A-betűvel kezdődik
    taxikSzama = len(azonositok)
    kivonni = 0
    for egy in azonositok:
        if egy.startswith("A") == True:
            szervizekSzama += 1

        if egy.endswith("X") == True and egy.find("0")>-1:
            kivonni +=1
    
    print(f"Összesen: {taxikSzama} db")
    print(f"Szervízek száma: {szervizekSzama} db")
    print(f"Flottából kivonni: {kivonni} db")

a = taxiAzonositokRogzitese()
taxiElemzes(a)

