import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            input_user = int(input("Level: "))
            if 1 <= input_user <= 3:
                return input_user
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        min_number, max_number = 0, 9
    elif level == 2:
        min_number, max_number = 10, 99
    elif level == 3:
        min_number, max_number = 100, 999
    else:
        return

    it_clock = 0
    for _ in range(10):
        random_number = random.randint(min_number, max_number)
        random_number2 = random.randint(min_number, max_number)
        correct_answer = random_number + random_number2
        error_count = 0

        while True:
            try:
                user_answer = int(input(f"{random_number} + {random_number2} = "))
                if user_answer != correct_answer:
                    print("EEE")
                    error_count += 1
                    if error_count == 3:
                        print(f"{random_number} + {random_number2} = {correct_answer}")
                        break
                else:
                    it_clock += 1
                    break
            except ValueError:
                print("EEE")

    print(f"Score: {it_clock}")

if __name__ == "__main__":
    main()
