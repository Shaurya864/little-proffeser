#Write a program to compute factorial of a number using for loop.
n=int(input("enter the number"))
fact=1
for i in range(n):
    fact=fact*(i+1)
print(f"factorial of the {n} will be {fact}")