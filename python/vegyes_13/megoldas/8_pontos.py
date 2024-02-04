import os
os.system("cls")

ft = int(input("Add meg hány Ft-ot szeretnél átváltani: "))
euro = int(input("Add meg hány Ft egy Euró: "))

ftInEur = round(ft/euro)

if ftInEur<100:
    kezelesiKtsg = 3
else:
    kezelesiKtsg = 0

osszeg = ftInEur-kezelesiKtsg

print(f"A {ft} Ft összege Euróban kerekítve: {ftInEur} €")
print(f"A kezelési kötlség összege: {kezelesiKtsg} €")
print(f"Átváltott összeg: {osszeg} €")