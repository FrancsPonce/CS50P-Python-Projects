import csv
import sys
import random



def main():
    return_value= function_argv()
    index_0,index_1,index_2,index_3 = function_csv(return_value)
    final_values= function_randomizer(index_0,index_1,index_2,index_3)

    if return_value == "EN":
        while True:
            user_input= input("Would you like some very particular advice from the ORACLE? (Y/N) : ")
            if user_input.upper() == "N":
                print( "I hope next time you come here, you are more decisive.")
                break
            elif user_input.upper() == "Y":
                print(final_values)
                break
            else:
                print(" Are you afraid of something? ...")
                continue

    elif return_value == "ES":

        while True:

            user_input= input("Te gustaria un particular consejo del ORACULO ? (S/N) : ")
            if user_input.upper() == "N":
                print(" Espero que la proxima vez te encuentres mas decidido.")
                break
            elif user_input.upper() == "S":
                print(final_values)
                break
            else:
                print(" Acaso tienes miedo alguno? ... ")
                continue

def function_argv():

    if len(sys.argv) < 2 :
            sys.exit("Too few arguments")
    elif len(sys.argv) > 2 :
            sys.exit("Too many arguments")

    try:
         if sys.argv[1].upper() == "EN":
              return "EN"
         elif sys.argv[1].upper() == "ES":
              return "ES"
         else:
              raise ValueError
    except ValueError:
         sys.exit("Need to select a LANGUAGE (EN/ES)")
    #except:
        #pass

def function_csv(s):

    index_0=[]
    index_1=[]
    index_2=[]
    index_3=[]

    if s == "EN":

         with open("EN.csv") as file:
              reader = csv.DictReader(file)
              for row in reader:
                   index_0.append(row ["index_0"])
                   index_1.append(row ["index_1"])
                   index_2.append(row ["index_2"])
                   index_3.append(row ["index_3"])

    elif s == "ES":

         with open("ES.csv") as file:
              reader = csv.DictReader(file)
              for row in reader:
                   index_0.append(row ["index_0"])
                   index_1.append(row ["index_1"])
                   index_2.append(row ["index_2"])
                   index_3.append(row ["index_3"])

    return index_0,index_1,index_2,index_3

def function_randomizer(i0,i1,i2,i3):

    first = random.choice(i0)
    second = random.choice(i1)
    thirth = random.choice(i2)
    fourth = random.choice(i3)

    return f"{first} {second} {thirth} {fourth} :)"



if __name__ == "__main__":
    main()
