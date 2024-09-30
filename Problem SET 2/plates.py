def main():
    plate = str(input("Plate: ")).upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        valid_character1= start_character(s)
        valid_character2= minmax_character(s)
        valid_character3= third_character(s)
        valid_character4= fourth_character(s)
        valid_character5= third2_character(s)
        #print(valid_character5)

        return valid_character1 and valid_character2 and valid_character3 and valid_character4 and valid_character5


# Def first condition

def start_character(u):
        letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for x in u[:2]:
            if x.isalpha():
                return True
            else:
                return False
# Def second condition
def minmax_character(u):
    if len(u) < 2 or len(u) >6:
         return False
    else:
         return True


def third_character(u):
    i = 0
    while i < len(u):
        if u[i].isdigit():
            if i + 1 < len(u) and u[i + 1].isalpha():
                return False
            #if u[i] == "0":
                #return False

        i += 1

    return True

def fourth_character(u):
     for x in u:
          if x in ["!", " ",".", "?"]:
               return False
     return True

def third2_character(u):
    i = 0
    while i < len(u):
        if u[i].isalpha():
            if i + 1 < len(u) and u[i + 1] == "0":
                return False
           
        i += 1
    return True


if __name__ == "__main__":
    main()
