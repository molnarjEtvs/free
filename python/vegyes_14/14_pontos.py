import os
os.system("cls")

def csapatRogzites():
    csapatok = []
    while True:
        csapat = input("Ellenfél csapat neve: ")
        if csapat == '':
            return csapatok
        else:
            csapatok.append(csapat.upper())

def pontszamitas(meccsek):
    meccsekSzama = len(meccsek)
    pontszam = 0
    for egyMeccs in meccsek:
        if egyMeccs.endswith('N') == True:
            pontszam+=1
    print(f"Meccsek darabszáma: {meccsekSzama} db")
    print(f"Elért pontszám: {pontszam} pont")

meccsek = csapatRogzites()
pontszamitas(meccsek)

'''
DEN
KC
HOU
TEN
MIN
'''