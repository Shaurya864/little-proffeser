#guesing game
import random

while True:
    level = input("Level: ")
    if level.isdigit():
        n = int(level)
        break
p = random.randint(1, n)
while True:
    guess = input("Guess: ")
    guess = int(guess)
    if guess < p:
        print("Too small!")
    elif guess > p:
        print("Too large!")
    else:
        print("Just right!")
        break
