#taxi útiköltség számolás
import os
os.system("cls")

alapDij = 1100
kmDij = 440
percDij = 110

kmSzama = round(float(input("Add meg hány km-t utaztál: ")))
percekSzama = int(input("Add meg hány percet utaztál: "))

percAr = percekSzama*percDij
kmAr = kmSzama*kmDij
utazasDija = alapDij+kmAr+percAr

print(f"A percdíj összesen: {percekSzama} perc / {percAr} Ft")
print(f"A km díj összesen: {kmSzama}km / {kmAr} Ft")
print(f"FIZETENDŐ ÖSSZEG: {utazasDija} Ft")