# Write a program to reverse digits of a given integer using a while loop.
n = int(input("Enter the number "))
rev=0
while n!=0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(f"Reversed number is {rev}")