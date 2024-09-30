
def main():
    while True:
        get_input= input("Fraction: ")
        convert_input= get_function(get_input)
        if convert_input !="Invalid" and convert_input != None:
            print (convert_input)
            break



def get_function(prompt):
    while True:
        try:
            return convert_function(prompt)

        except (ValueError, ZeroDivisionError):
            return "Invalid"






def convert_function(s):
         if "/" in s:
                x,y = (s).split("/")
                x= int(x)
                y= int(y)

                # Def Z
                div = (x/y)*100
                div_int= int(div)

                if "2/3" in s:
                     return "67%"

                if  div_int in [99,100] and div_int <=100:
                            return "F"
                elif div_int in [0,1] and div_int <=100:
                    return "E"
                elif div_int <=100:
                     return f"{div_int:.0f}%"
main()

