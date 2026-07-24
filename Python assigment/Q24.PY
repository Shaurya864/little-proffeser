#Write a program to remove duplicates from a list.
def remove_duplicates(items):
    return list(set(items))


nums = [1, 2, 2, 3, 4, 4, 5]
print("List without duplicates:", remove_duplicates(nums))
