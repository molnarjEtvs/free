import os
os.system("cls")

gombocAr = int(input("Mennyibe kerül egy gombóc fagyi: "))
tolcserAr = int(input("Mennyibe kerül egy  tölcsér: "))
gombocokSzama = int(input("Hány gombócot szeretnél venni: "))

if gombocokSzama>3:
    tolcserAr = 0

fizetenedo = (gombocAr*gombocokSzama)+tolcserAr

print(f"{gombocokSzama} gombóc fagylalt tölcsérrel együtt {fizetenedo} Ft lesz.")