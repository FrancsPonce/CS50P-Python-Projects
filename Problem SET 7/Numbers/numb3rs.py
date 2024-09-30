import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        split_numbers = ip.split(".")
        for i in split_numbers:
            if not (0 <= int(i) <= 255):
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
