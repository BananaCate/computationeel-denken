organismen: float = float(input("Start aantal organismen "))
procent_groei: float = float(input("Procentuele dagelijkse groei "))/100 +1
dagen: int = int(input("Aantal dagen "))

print("Dag        Populatie")
for i in range(dagen):
    dag: int = i+1
    if dag < 10:
        print(dag, (8*" "), round(organismen, 2))
    else:
        print(dag, (7*" "), round(organismen, 2))
    organismen *= procent_groei