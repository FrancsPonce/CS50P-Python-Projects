
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regexformat= re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)

    if regexformat:
        x = regexformat.groups()
        if int(x[1])>12 or int(x[5])>12:
            raise ValueError
        first = convert_format(x[1],x[2],x[3])
        second = convert_format(x[5],x[6],x[7])

        return first + " to " + second



    else:
        raise ValueError



def convert_format(h, m, am_pm):

    if am_pm == "PM":
        if int(h) == 12:
            new_h = 12
        else:
            new_h= int(h)+12
    else:
        if int(h) == 12:
            new_h = 0
        else:
            new_h = int(h)

    if m == None:
        new_m = ":00"
        time_convert= f"{new_h:02}"  + new_m
    else:
        time_convert= f"{new_h:02}" + ":" + m

    return time_convert

...


if __name__ == "__main__":
    main()
