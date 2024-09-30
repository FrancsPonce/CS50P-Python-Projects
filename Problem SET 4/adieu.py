import inflect
p = inflect.engine()

list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print()
        break

result= p.join(list)
print("Adieu, adieu, to " + result)

