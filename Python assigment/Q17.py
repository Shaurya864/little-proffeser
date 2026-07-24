#. Write a Python program to count vowels and consonants in a string.
s=input("Enter the String : ")
count=0
vowelcount=0
vowels= "AEIOUaeiou"
for i in s :
    if i.isalpha():
        if i in vowels:
            vowelcount=vowelcount +1
        else:
            count=count+1
    
print(f"given string has {vowelcount} vowels and {count} consonants")
