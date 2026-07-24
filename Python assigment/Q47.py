#Write a program to generate random passwords using random module.
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("Random Password:", generate_password(12))