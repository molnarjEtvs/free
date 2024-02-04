#hiteltörlesztő részlet számolása
import os
os.system("cls")

felvettOsszeg = int(input("Add meg a felvett összeget: "))
futamido = int(input("Add meg futamidőt (hónap):"))
thm = float(input("Add meg a THM-et (%): "))

visszafizetendo = (felvettOsszeg*(thm/100+1))
haviTorleszto = round((visszafizetendo/futamido))

print(f"Visszafizetendő összeg: {visszafizetendo} Ft")
print(f"Havi törlesztő részlet: {haviTorleszto} Ft")