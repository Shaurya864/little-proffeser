a = int(input("Enter T-A_1 marks = "))
b = int(input("Enter Mid Sem Marks = "))
c = int(input("Enter TA-2 Marks = "))

# Marks needed in End Sem to reach total of 200
e = 200 - (a + b + c)

def checkgrade(e):
    if 90 <= e <= 100:
        print("A+ is possible")
    elif 80 <= e < 90:
        print("A is possible")
    elif 70 <= e < 80:
        print("B+ is possible")
    elif 60 <= e < 70:
        print("B is possible")
    elif 50 <= e < 60:
        print("C+ is possible")
    else:
        print("Grade not possible with required marks")

# 🔹 Call the function here
checkgrade(e)