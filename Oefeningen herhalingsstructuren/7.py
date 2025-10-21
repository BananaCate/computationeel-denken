reistijd: int = int(input("Hoe lang reis je? (in uur) "))
snelheid: int = int(input("Hoe snel reis je? (ik km/u) "))
afgelegde_afstand: int = 0
print ("Uur        Afgelegde afstand")
for i in range(1,reistijd+1):
    afgelegde_afstand = i* snelheid
    if i < 10:
        print(i, " " * 8, afgelegde_afstand)
    else:
        print(i, " " * 7, afgelegde_afstand)
