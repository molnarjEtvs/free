import os
os.system("cls")


def termekBekeres():
    termekek = []
    while True:
        ar = int(input("Add meg a termék árát: "))
        if ar == 0:
            return termekek
        elif ar<0:
            ar = ar*-1
        termekek.append(ar)

def kiszamolas(termekek):
    ossz = sum(termekek)
    atlag = ossz/len(termekek)
    parosakOszsege = 0
    for t in termekek:
        if t%2==0:
            parosakOszsege += t
    print(f"Termékek összértéke: {ossz} Ft")
    print(f"Átlag érték: {atlag} Ft")
    print(f"Párosak összege: {parosakOszsege} Ft")



termekek = termekBekeres()
kiszamolas(termekek)