#Write a function with default arguments to compute area of rectangle.
def area_rectangle(length=5, width=3):
    return length * width

print("Default area:", area_rectangle())
print("Custom area:", area_rectangle(10, 4))