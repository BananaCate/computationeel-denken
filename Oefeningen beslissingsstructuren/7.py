massa: float = float(input("Hoeveel weegt je pakketje in kg? "))
if massa < 3:
    print("De tarrief is €5")
elif massa < 7:
    print("De tarrief is €10")
elif massa < 11:
    print("De tarrief is €15")
else:
    print("De tarrief is €20")