#Write a program to extract all numbers from a given text using regex
import re

def extract_numbers(text):
    
    numbers = re.findall(r'\d+', text)
    return numbers


sentence = "Shaurya scored 95 marks in Math and 88 in Science."
print("Extracted numbers:", extract_numbers(sentence))