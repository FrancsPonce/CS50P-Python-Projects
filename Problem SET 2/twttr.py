def main():
    x = input ("Input: ")
    x1= convert(x)
    print(x1)




def convert(u):
    lista= ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    result=""
    for x in u:
        if x not in lista:
            result += "" + x



    return result

main()
