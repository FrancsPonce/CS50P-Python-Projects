import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count_um = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(count_um)

...


if __name__ == "__main__":
    main()
