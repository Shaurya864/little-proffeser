#Write a program to replace all whitespace with a single space in a sentence
import re

def normalize_whitespace(text):
    
    return re.sub(r'\s+', ' ', text).strip()


sentence = "This   is   a   sentence \t with   irregular   spacing."
print("Normalized sentence:", normalize_whitespace(sentence))