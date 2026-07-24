#Write a program using decorators to add logging before function call.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")


greet("Shaurya")