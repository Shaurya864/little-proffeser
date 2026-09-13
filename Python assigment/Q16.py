#Write a program to calculate command-line sum of integer arguments using sys.argv[].
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <num1> <num2> ...")
        return
    
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]  # convert arguments to integers
        total = sum(numbers)
        print("Sum of arguments =", total)
    except ValueError:
        print("Error: Please provide only integer arguments.")

if __name__ == "__main__":
    main()