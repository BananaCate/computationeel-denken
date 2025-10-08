seconden: int = int(input("Voer een aantal seconden in "))
dagen: int = seconden // 86400
uren: int = (seconden // 3600) - dagen * 24
minuten: int = (seconden // 60) - uren * 60 - dagen * 24*60
seconden = seconden - minuten * 60 - uren * 3600 - dagen * 86400

if dagen:
    print (dagen, "dagen", uren, "uren", minuten, "minuten", seconden,"seconden")
elif uren:
    print (uren, "uren", minuten, "minuten", seconden,"seconden")
elif minuten:
    print ( minuten, "minuten", seconden,"seconden")
else:
    print (seconden,"seconden")