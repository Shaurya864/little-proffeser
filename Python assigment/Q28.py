#Write a program to merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}


merged = dict1.copy()
merged.update(dict2)


merged2 = {**dict1, **dict2}

print("Merged dictionary:", merged)
print("Merged dictionary (unpacking):", merged2)
