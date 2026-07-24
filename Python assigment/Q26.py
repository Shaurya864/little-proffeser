#Write a program to convert list to tuple and vice versa.
def list_to_tuple(lst):
    return tuple(lst)


def tuple_to_list(tpl):
    return list(tpl)

my_list = [1, 2, 3, 4]
my_tuple = list_to_tuple(my_list)
print("List to Tuple:", my_tuple)

new_list = tuple_to_list(my_tuple)
print("Tuple to List:", new_list)
