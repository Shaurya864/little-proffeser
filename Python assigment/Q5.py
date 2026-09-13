# Q5 Write a program to perform all arithmetic, relational, logical, and bitwise operations.

a=int(input("enter 1 st number: "))
b=int(input("Enter 2nd number : "))
# Arithmetic

print(f"addition :{a+b}")
print(f"subtraction :{a-b}")
print(f"multiplication :{a*b}")
print(f"division :{a/b}")
#relational 
print(a == b)   
print(a != b)  
print(a > b)   
print(a < b)   
print(a >= 10) 
print(b <= 15) 
#logical
print(a > 5 and b > 15)   
print(a > 15 or b > 15)   
print(not(a > b))    
#bitwise
print(a & b)   
print(a | b)   
print(a ^ b)   
print(~a)      
print(a << 1)  
print(a >> 1)  
     

