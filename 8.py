aantal_seconden: int = int(input("Geef een aantal seconden in "))
aantal_uren: int = aantal_seconden//3600
aantal_minuten: int = aantal_seconden//60 - aantal_uren*60
aantal_seconden = aantal_seconden - aantal_minuten*60 - aantal_uren*3600
print ("Dat komt overeen met:", aantal_uren, "u", aantal_minuten, "min", aantal_seconden, "s")