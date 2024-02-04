import os
os.system('cls')

meccsekSzam = int(input("Add meg hány meccset játszott: "))
golokSzama = int(input("Add meg hány gólt lőtt a játékos: "))

atlag = round(meccsekSzam/golokSzama)

if atlag<=20:
    fizetes = 0
else:
    fizetes = atlag*23

print(f"A játékos gólainak száma: {golokSzama} db, meccsek száma: {meccsekSzam} db")
print(f"Átlagos gólok száma: {atlag} db")
print(f"A játékos fizetése: {fizetes} Ft")