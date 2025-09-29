#Voor het bakken van 48 koekjes zijn de volgende ingrediënten nodig:
#• 250 gr suiker
#• 200 gr boter
#• 4 eieren
#• 300 gr bloem
#Schrijf een programma dat de gebruiker vraagt hoeveel koekjes hij wilt bakken. Hierna wordt
#weergegeven hoeveel hij van elke ingrediënt nodig heeft.
aantal_koekjes: int = int(input("Hoeveel koekjes wil je bakken?"))
factor: float = 48/aantal_koekjes
print("De hoeveelheid gram suiker dat je nodig hebt is:", (250/ factor))
print("De hoeveelheid gram boter dat je nodig hebt is:", (200/ factor))
print("De hoeveelheid eieren dat je nodig hebt is:", (4/ factor))
print("De hoeveelheid gram bloem dat je nodig hebt is:", (300/ factor))

# er werd niets gezegd over afrondingen en zo