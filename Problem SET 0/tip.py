def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")





def dollars_to_float(d=str):
    convert=str(d).replace("$","")
    convert1= float(convert)
    convert_rounded= round((convert1), 2)
    convert_rounded2= str(convert_rounded)
    print (convert_rounded2)
    return convert_rounded2
    # TODO



def percent_to_float(p=str):
    convert2= str(p).replace("%","")
    convert2_integer=int(convert2)
    convert2_percentage= convert2_integer/100
    convert2_full= str(convert2_percentage)
    #convert2_rounded= round((convert2_percentage), 2)
    print (convert2_percentage)
    return convert2_full
    # TODO


main()
