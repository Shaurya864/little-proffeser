import random

def get_level():
    while True:
        try:
            level = int(input("Choose level (1:Add, 2:Sub, 3:Mul, 4:Div): "))
            if level in [1, 2, 3, 4]:
                return level
            else:
                print("Please choose a valid level between 1 and 4.")
        except ValueError:
            print("Enter a number!")

def generate_integer():
    level = get_level()
    p = random.randint(1, 10)
    q = random.randint(1, 10)

    if level == 1:
        correct = p + q
        symbol = "+"
    elif level == 2:
        correct = p - q
        symbol = "-"
    elif level == 3:
        correct = p * q
        symbol = "X"
    elif level == 4:
        p = p * q  # Ensures clean division
        correct = p // q
        symbol = "/"

    attempts = 0
    while attempts < 3:
        try:
            guess = int(input(f"{p} {symbol} {q} = "))
            if guess == correct:
                print("Correct!")
                break
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("Enter a number!")
            attempts += 1

    if attempts == 3:
        print("Answer:", correct)

def main():
    generate_integer()

main()