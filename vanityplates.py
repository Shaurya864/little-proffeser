def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: No periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    # Rule 4: Numbers must be at the end, not in the middle
    for i in range(len(s)):
        if s[i].isdigit():
            # Once a digit appears, everything after must be digits
            if not s[i:].isdigit():
                return False
            # Rule 5: First number cannot be '0'
            if s[i] == '0':
                return False
            break

    return True


main()
    
