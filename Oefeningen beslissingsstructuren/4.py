jaar: int = int(input("Geef een jaartal in "))
if jaar % 400 == 0 or (jaar % 100 != 0 and jaar % 4 == 0):
    print("het jaar", jaar, "is een schrikkeljaar")
else:
    print("het jaar", jaar, "is geen schrikkeljaar")