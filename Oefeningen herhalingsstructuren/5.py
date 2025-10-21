budget: float = float(input("Wat is je budget? "))
nogKopen: bool = True
while nogKopen:
    budget -= float(input("Hoeveel kost dit product "))
    nogKopen = "J" == input("Heb je nog producten die je wilt kopen? ")
if budget >= 0:
    print("Je overige budget is", budget)
else:
    print("Je zit in het rood! Je budget is", budget)