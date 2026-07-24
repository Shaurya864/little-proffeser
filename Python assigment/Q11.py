#Write a program to generate the multiplication table for a given number.
n=int(input("enter the number of multiplication"))
print("<--Multiplication table till 10-->")
for i in range(11):
    print(f"{n} X {i} = {n*i}")