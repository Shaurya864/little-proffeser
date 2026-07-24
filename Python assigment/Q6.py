# Q6 Write a program to find the maximum of three numbers using nested if–else
a=int(input("enter a: "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
if a>b and a>c:
    print("a is greatest of all ")
elif a>b and a==c:
    print("a is greatest of all ")
elif b>a and a==c:
    print("b is greatest of all ")
elif b>a and b>c:
    print("b is greatest of all ")
elif c>a and c==b:
    print("c is greatest of all ")
elif c>a and c>b:
    print("c is greatest of all ")
elif a==b==c:
    print("All are equal")
elif a==c and b<a:
    print("a is greatest of all ")
elif a==b and b<c:
    print("c is greatest of all ")
elif a==b and b>c:
    print("a nd b is greatest of all ")



