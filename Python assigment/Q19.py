#Write a program to check palindrome string.
def is_palindrome(text):
    
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    
    return cleaned_text == cleaned_text[::-1]



input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
