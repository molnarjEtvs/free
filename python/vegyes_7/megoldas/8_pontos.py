import os
os. system("cls")

oraDb = int(input("Add meg hány darab óra volt: "))
hianyDb = int(input("Add meg hány darab hiányzásod volt: "))
szazalek = (hianyDb/oraDb)*100
print(f"Hiányzás aránya: {szazalek}%")
if szazalek>=20:
    print("Pótolnod kell az órákat! Nagy bajban vagy!")
elif szazalek>=10:
    print("Ne hiányozz többet mert pótolnod kell!")
else:
    print("Minden rendben van!")