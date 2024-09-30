import sys

count_lines = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith("#") or line.isspace():
                        pass
                    else:
                        count_lines += 1
        except:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

print(count_lines)
