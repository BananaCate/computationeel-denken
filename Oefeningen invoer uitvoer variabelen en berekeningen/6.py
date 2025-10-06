prijs1: float = float(input("Voer hier het prijs van de eerste artikel in: "))
prijs2: float = float(input("Voer hier het prijs van de tweede artikel in: "))
prijs3: float = float(input("Voer hier het prijs van de derde artikel in: "))
prijs4: float = float(input("Voer hier het prijs van de vierde artikel in: "))
prijs5: float = float(input("Voer hier het prijs van de vijfde artikel in: "))
som: float = prijs1 + prijs2 + prijs3 + prijs4 + prijs5
getaxte_som: float = som * 1.21
print ("de prijs van alle 5 artikelen zonder BTW is", som, ", inclusief BTW kost het", getaxte_som)