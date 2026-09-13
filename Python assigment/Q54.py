# Write a program to validate phone numbers using regex.
import re

def validate_phone(number):
    
    pattern = r'^[6-9]\d{9}$'
    
    if re.match(pattern, number):
        return True
    else:
        return False


phone = input("Enter a phone number: ")
if validate_phone(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")