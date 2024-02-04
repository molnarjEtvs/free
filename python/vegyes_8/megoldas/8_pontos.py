import os
os.system("cls")

eletKor = int(input("Add meg az életkorod: "))
kezdoE = input("Kezdő vagy-e? ")

if kezdoE == "I":
    felsoSzorzo = 0.8
else:
    felsoSzorzo = 0.7

alsoHatar = (220-eletKor)*0.65
felsoHatar = (220-eletKor)*felsoSzorzo

print(f"A kardió edzéshez a megfelelő pulzus intervallumod: {alsoHatar}-{felsoHatar}/perc")