# Write a program to sort a list of tuples based on the second element.
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])


data = [(1, 4), (3, 1), (2, 5), (7, 2)]
print("Sorted list:", sort_by_second(data))

