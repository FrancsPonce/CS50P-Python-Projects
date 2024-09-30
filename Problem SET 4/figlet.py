from pyfiglet import Figlet
import sys
import random


def main():

    figlet = Figlet()
    try:

        if len(sys.argv)==3 and sys.argv[1] in ["-f", "--font"]:
                sys.argv[2] = f"{sys.argv[2]}"
                #print (sys.argv[2])
                figlet.setFont(font=sys.argv[2])
                input_user= input("Input: ")
                print(f"Output:\n {figlet.renderText(input_user)}")

        elif len(sys.argv)==1:
            input_user= input("Input: ")
            font_get= random.choice(figlet.getFonts())
            figlet.setFont(font=font_get)
            print(f"Output:\n {figlet.renderText(input_user)}")
        else:
             sys.exit(1)
    except:
        print("Invalid usage")
        sys.exit(1)

main()

