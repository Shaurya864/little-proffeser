# Write a program to demonstrate the use of break, continue, and pass statements.
print("Demonstrating break:")
for i in range(1, 6):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("\nDemonstrating continue:")

for i in range(1, 6):
    if i == 3:
        print("Skipping iteration at i =", i)
        continue
    print("i =", i)

print("\nDemonstrating pass:")
# Using pass
for i in range(1, 6):
    if i == 3:
        print("Pass statement executed at i =", i)
        pass  
    print("i =", i)
