saldo: float = float(input("Geef het saldo in euro dat op je rekening staat: "))
interestpercentage: float = float(input("Geef het intrestpercentage: "))
interest: float = saldo * (interestpercentage/100)
print ("Je krijgt jaarlijks", round(interest, 2), "euro op deze spaarrekening")
som: float = interest + saldo
print ("Met jaarlijkse intrest erbij staat er", round(som, 2), "euro op deze spaarrekening")