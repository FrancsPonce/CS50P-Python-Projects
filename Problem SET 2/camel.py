def main():
    x= input ("camelCase: ")
    x1 = mayusfind(x)
    x2= x1.lower()
    print(f"snake_case: {x2}")


def mayusfind(u):
    result = ""
    for i, x in enumerate(u):
        if x.isupper() and i !=0:
            result += "_" + x
        else:
            result += x
    return result


main()
