# Write a program to find the largest and smallest number in a list
def find_min_max(numbers):
    return min(numbers), max(numbers)


nums = [5, 12, 7, 25, 3]
smallest, largest = find_min_max(nums)
print("Smallest:", smallest)
print("Largest:", largest)
