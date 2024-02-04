import os
os.system("cls")

def tabletGyartok():
    tabletek = []
    while True:
        tablet = input("Add meg a tablet gyártóját: ")
        if tablet == "":
            return tabletek
        else:
            tabletek.append(tablet.capitalize())


def tabletStatisztika(tabletek):
    db = len(tabletek)
    dbStartA = 0
    dbEndE = 0
    dbFindNo = 0
    for tab in tabletek:
        if tab.startswith("A") == True:
            dbStartA+=1
        if tab.endswith("e") == True:
            dbEndE+=1
        if tab.find("no")>-1:
            dbFindNo+=1
    print(f"Darabszám: {db} db")
    print(f"A-betűvel kezd: {dbStartA} db")
    print(f"E-betűvel végez: {dbEndE} db")
    print(f"no találat: {dbFindNo} db")

t = tabletGyartok()
tabletStatisztika(t)
'''
apple
realme
acer
lenovo
alcatel
ulefone
honor
'''