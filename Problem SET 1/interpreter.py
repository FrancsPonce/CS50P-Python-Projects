

def functions_methods():
    #Geting the input
    expression= input("Expression: ")
    #Creating the partitions
    x, y, z= expression.split(" ")
    #Parts
    x = int(x)
    z = int(z)

    # Defining Y

    suma = x + z
    resta = x - z
    div = x/z
    mult = x*z




    if y == "+":
        print (f"{suma:.1f}" )
    elif y == "-":
        print (f"{resta:.1f}" )
    elif y == "/":
        print (f"{div:.1f}" )
    elif y == "*":
        print (f"{mult:.1f}" )
    else:
        print("Write a correct aritmetic function")



functions_methods()
