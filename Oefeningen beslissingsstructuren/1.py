leeftijd: int = int(input("Wat is jouw leeftijd? "))
if leeftijd < 2:
    print("Je bent een baby")
elif leeftijd < 13:
    print("Je bent een kind")
elif leeftijd < 18:
    print("Je bent een minderjarige tiener")
elif leeftijd < 20:
    print("Je bent een meerderjarige tiener")
else:
    print ("Je bent een volwassene")