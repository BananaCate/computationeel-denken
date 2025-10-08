gewicht: int = int(input("Wat is je gewicht in kg? "))
lengte: float = float(input("Wat is je lengte in meter? "))
bmi:float = float(gewicht) / (lengte**2)

if bmi < 18.5:
    print("Je hebt ondergewicht")
elif 18.5 <= bmi <= 25:
    print("Je hebt een ideaal gewicht")
else:
    print("Je hebt overgewicht")