#. Write a program to sort dictionary items by key and by value
data = {"banana": 3, "apple": 5, "cherry": 2}


sorted_by_key = dict(sorted(data.items()))


sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted by key:", sorted_by_key)
print("Sorted by value:", sorted_by_value)

