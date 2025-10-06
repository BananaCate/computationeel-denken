# bereken de punten op 20 om naar hun vak maximum
# bereken met dit perentage op de totaal hoeveelheid puntenµ
# tell alle totaal percentages op en neem het gemiddelde

wisk: float = float(input("Geef je punten op 20 voor wiskunde: "))
informatica: float = float(input("Geef je punten op 20 voor informatica: "))
fysica: float = float(input("Geef je punten op 20 voor fysica: "))

wisk_totaal: float = (wisk/20) * 130
informatica_totaal: float = (informatica/20) * 150
fysica_totaal: float = (fysica/20) * 80

wisk_percent: float = wisk_totaal/360
informatica_percent: float = informatica_totaal/360
fysica_percent: float = fysica_totaal/360

som_percent: float = format((wisk_percent + informatica_percent + fysica_percent),".0%")
print(som_percent)