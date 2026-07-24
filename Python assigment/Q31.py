#Write a program to create an ordered dictionary.
ordered_dict = {}


ordered_dict["banana"] = 3
ordered_dict["apple"] = 5
ordered_dict["cherry"] = 2

print("Ordered Dictionary:", ordered_dict)


print("Items in order:")
for key, value in ordered_dict.items():
    print(key, ":", value)

