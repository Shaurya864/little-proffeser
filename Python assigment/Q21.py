#Write a program to find frequency of characters in a string using a dictionary.
def char_frequency(text):
    freq_dict = {}  
    
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1    # increment if already exists
        else:
            freq_dict[char] = 1     # initialize if first time
    
    return freq_dict


# Driver code
input_string = input("Enter a string: ")
frequency = char_frequency(input_string)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
