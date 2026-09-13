#Write a program to accept marks and display the grade using if–elif–else
marks=int(input("Enter marks:"))
if marks>=90:
    print("Grade A+")
elif marks>=80:
    print("Grade A")
elif marks >=70:
    print("Grade B+")
elif marks >=60:
    print("Grade B")
elif marks>=50:
    print("Grade C+")
else:
    print("Grade F")