aantal: int = int(input("Hoeveel exexmplaren van het softwarepakket wil je? "))
prijs: float = 99*aantal
if 10 <= aantal < 20:
    print("De originele prijs is", prijs)
    prijs *= 0.9
elif aantal >= 20:
    print("De originele prijs is", prijs)
    prijs *= 0.8

print("De prijs is :", prijs)