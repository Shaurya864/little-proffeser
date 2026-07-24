#Write a program to find all words starting with a capital letter
import re

def find_capital_words(text):
    
    words = re.findall(r'\b[A-Z][a-z]*\b', text)
    return words


sentence = "Shaurya Loves Python And Gaming."
print("Words starting with capital letters:", find_capital_words(sentence))