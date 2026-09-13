#Write a program to calculate sum of N natural numbers using a for loop.
n= int(input("Enter the number till we want sum :"))
sum =0
for i in range (n+1):
    sum=sum+i
print(f"Sum of {n}th number is {sum}")
