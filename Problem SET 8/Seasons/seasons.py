from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_input= input("Date of Birth: ")
    try:
        y, m, d = check_format(birth_input)

    except:
        sys.exit("Invalid Date")

    date_birth= date(int(y), int(m), int(d))
    #print(date_birth)
    date_today= date.today()
    #print(date_today)
    convert= date_today - date_birth
    #print(convert)
    totalminutes= convert.days * 24 * 60
    final_convert= p.number_to_words(totalminutes, andword="")
    print (final_convert.capitalize() + " minutes")



def check_format(birthdate):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birthdate):
        y, m , d= birthdate.split("-")
        return y,m,d




...


if __name__ == "__main__":
    main()
