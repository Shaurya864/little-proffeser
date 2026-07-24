# Write a program to demonstrate array creation and operations using array module
import array


arr = array.array('i', [10, 20, 30, 40])

print("Original array:", arr)


arr.append(50)
print("After append:", arr)


arr.insert(2, 25)
print("After insert:", arr)


arr.remove(30)
print("After remove:", arr)


print("Element at index 1:", arr[1])
