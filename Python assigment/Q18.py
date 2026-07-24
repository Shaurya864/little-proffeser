#Write a program to reverse a string without using slicing.
def reverse_string(text):
    reversed_text = ""  
    
    
    for char in text:
        reversed_text = char + reversed_text  
    
    return reversed_text



input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))
