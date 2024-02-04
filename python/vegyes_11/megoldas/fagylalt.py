import os
os.system("cls")

def fagylaltNevek():
    fNevek = []
    while True:
        nev = input("Kérem a fagylalt nevét: ")
        if nev != "":
            fNevek.append(nev)
        else:
            return fNevek
        
def Statisztika(fNevek):
    db = len(fNevek)
    veganDb = 0
    for egyNev in fNevek:
        if egyNev.find("vegán") >-1:
            veganDb += 1
    print(f"{db} féle fagyi kapható.")
    print(f"Ebből vegán ízesítésű: {veganDb} db")

n = fagylaltNevek()
Statisztika(n)

