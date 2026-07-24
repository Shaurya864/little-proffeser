#Write a program to check whether a year is leap year or not
year=int(input("Enter the year : "))
if year %400 ==0 or year %100!=0 and year %4==0:
    print(f"{year} is leap ")
else:
    print(f"{year} is not a leap year")
    