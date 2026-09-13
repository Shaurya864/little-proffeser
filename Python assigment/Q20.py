#Write a program to remove all punctuation from a string.
import string


def remove_punctuation(text):
   
    punctuation_set = set(string.punctuation)
    
    
    cleaned_text = "".join(char for char in text if char not in punctuation_set)
    
    return cleaned_text



input_string = input("Enter a string: ")
print("String without punctuation:", remove_punctuation(input_string))
