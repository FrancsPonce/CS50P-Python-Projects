
import sys
import csv
from tabulate import tabulate

def main():
    argv_function()

    list=[]

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(list[1:], headers=list[0], tablefmt="grid"))

def argv_function():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a csv file")

if __name__== "__main__":
    main()
