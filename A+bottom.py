s=input("Enter Subject =")
a=int(input("Enter T-A_1 marks = "))
b=int(input("Enter Mid Sem Marks = "))
c=int(input("Enter TA-2 Marks="))
e=200-a-b-c
g=input("Which Grade you want to pursue")
print(f"<---{s}--->")

    
def final(g):
    
    if g=="A+": m=e-20
    if g=="A" : m=e-40
    if g=="B+" : m=e-60
    if g=="B":  m=e-80
    if g=="C+":m=e-100
    if m>100:
        print(f"{g} cannot be acheive in {s}")
    else:
        print(f"To get {g} grade you should acheive {m}+ out of 100 in final exam")

final(g)

