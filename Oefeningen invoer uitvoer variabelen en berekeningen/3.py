# F = C * 9/5 + 32
celcius: float = float(input("Geef de temperatuur op in °C:"))
farenheight: float = celcius*9/5 + 32

print (str(celcius) + "°C is", str(farenheight) + "°F") # standaart spaties weg
# print (celcius, "°C is", farenheight, "°F") # met standaart spaties