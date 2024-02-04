import os
os.system("cls")
def telefonHivasokRogzitese():
    hivasok = []
    while True:
        start = int(input("Add meg a hivás kezdő percét: "))
        if start == 0:
            break
        stop = int(input("Add meg a hivás vég percét: "))
        if start<stop:
            egyHivas = {}
            egyHivas['start'] = start
            egyHivas['stop'] = stop
            egyHivas['ido'] = stop-start
            hivasok.append(egyHivas)
            print("Hívás rögzítve!")
        else:
            print("Hívás NINCS rögzítve, mert a kezdő percnek kissebbnek kell lennie a vég percnél!")
    return hivasok

def telefonHivasokKieertekeles(hivasok):
    osszperc = 0
    db = len(hivasok)
    leghosszabbHivas = 0
    for egyHivas in hivasok:
        osszperc+=egyHivas['ido']
        if leghosszabbHivas<egyHivas['ido']:
            leghosszabbHivas=egyHivas['ido']
    atlag = osszperc/db
    print(f"Az összes telefonálással összesen perc: {osszperc} perc")
    print(f"Az átlag hívás időtartalma: {atlag} perc")
    print(f"A leghosszabb hívás: {leghosszabbHivas} perc")

hivasok = telefonHivasokRogzitese()
telefonHivasokKieertekeles(hivasok)