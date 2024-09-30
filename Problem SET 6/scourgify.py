import sys
import csv


def main():
    check_argv()
    list=[]
    try:
        with open(sys.argv[1], "r") as file:
            dict_reader= csv.DictReader(file)
            for row in dict_reader:
                split_name= row["name"].split(", ")
                list.append({"first": split_name[1].lstrip(), "last":split_name[0], "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as newfile:

            writer = csv.DictWriter(newfile, fieldnames=(["first","last","house"]))
            writer.writeheader()
            for row in list:
                writer.writerow({"first": row["first"], "last": row["last"], "house":row["house"]})

def check_argv():

    if len(sys.argv) >3 :
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("File is no CSV")


if __name__ == "__main__":
    main()
