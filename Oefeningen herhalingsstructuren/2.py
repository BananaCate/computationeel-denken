for i in range(25):
    jaar: int = i+1
    if jaar < 10:
        print ("Jaar", jaar, "", 1.74*jaar,"mm") # ,"",  voegt een spatie toe doordat er een lege element geprint wordt
    else:
        print ("Jaar", jaar, 1.74*jaar,"mm")