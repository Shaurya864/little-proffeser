# Write a function to demonstrate variable-length arguments.
def display_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


display_args(1, 2, 3, name="Shaurya", age=21)