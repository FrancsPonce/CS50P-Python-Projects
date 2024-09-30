
def working():


    cents= [25,10,5]


    results= int(50)

    while results>0:
        print (f"Amount Due: {results}")
        n = int(input("Insert Coin: "))
        if n in cents:
            results -= n
        else:
            continue

        if results <= 0:
           print (f"Change Owed: {results*-1}")
           break

working()

