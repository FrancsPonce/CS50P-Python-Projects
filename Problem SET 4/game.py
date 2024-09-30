import random

random_number = random.randint(1, 100)

while True:
    try:
        input_user = int(input("Level: "))
        random_number = random.randint(1, input_user)
        if 0 < input_user:
            while True:
                try:
                    second_input = int(input("Guess: "))
                    if second_input > random_number and 0 < second_input :
                        print("Too large!")

                    elif second_input < random_number and 0 < second_input :
                        print("Too small!")

                    elif second_input == random_number and 0 < second_input:
                        print("Just right!")
                        break
                except ValueError:
                    pass
            break
    except ValueError:
        pass
