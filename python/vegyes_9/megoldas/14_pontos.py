#törlesztő részlet 
import os
os.system("cls")

def torlesztoRogzites():
    torlesztesek = []
    sorszam = 1
    while True:
        torleszto = int(input(f"Add meg a(z) {sorszam}. törlesztő részletet: "))
        sorszam+=1
        if torleszto!=0:
            torlesztesek.append(round(torleszto*0.9))
        else:
            return torlesztesek
        
def torlesztoStatisztikak(torlesztesek):
    db = len(torlesztesek)
    legkisebb = min(torlesztesek)
    legnagyobb = max(torlesztesek)
    osszesBefizetes = sum(torlesztesek)
    atlag = round(osszesBefizetes/db)
    otvenAlattiDb = 0
    for egy in torlesztesek:
        if egy<50000:
            otvenAlattiDb+=1
    print(f"Befizetések száma: {db} db")
    print(f"Legalacsonyabb törlesztő: {legkisebb} Ft")
    print(f"Legmagasabb törlesztő: {legnagyobb} Ft")
    print(f"Összbefizetés: {osszesBefizetes} Ft")
    print(f"Átlag befizetés: {atlag} Ft")
    print(f"50.000 Ft alatti befizetések száma: {otvenAlattiDb} db")

t = torlesztoRogzites()
torlesztoStatisztikak(t)



