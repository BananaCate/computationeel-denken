getal: int = int(input("Geef een getal in waarvan je de faculteit wilt "))
faculteit: int = 1
for i in range(getal):
    faculteit *= i+1
print(str(getal) + "! =", faculteit)