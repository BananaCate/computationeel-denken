personen: int = int(input("Hoeveel mensen zijn er? "))
worsten: int = (personen // 11) + 1 # 1 pak is altijd nodig, maar per meervoud van 11 personen moet er een pak meer
broodjes: int = (personen // 9) + 1
r_worsten: int = worsten*10 - personen
r_broodjes: int = broodjes*8 - personen

print("Aantal worsten pakjes nodig:", worsten)
print("Aantal broodjes pakjes nodig:", broodjes)
print("Aantal worsten pakjes over:", r_worsten)
print("Aantal broodjes pakjes over:", r_broodjes)