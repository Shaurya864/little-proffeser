import random
score=0
def main():
    global score
    l=get_level()
    x=int(input("How much Question U want to Ask ? \n"))
    for _ in range(x):
        generate_integer(l)
        
    print(f"marks score out of {x}: ",score)
    y=score*100
    y=y/x
    y=int(y)
    if y>=90:
        print("Grade A")
    elif y>=80:
        print("Grade B")
    elif y>=70:
        print("Grade C")
    elif y>=60:
        print("Grade D")
    elif y>=50:
        print("Grade E")
    else:
    
        print("Grade F")
    print(f"percentage scored:{float(y)}%\n")
    
def get_level():
    l=0
    list=[1,2,3,4]
    while l not in list and l==int(l):
        print("<---Little Professer--->")
        print("Press 1 for Addition\n")
        print("Press 2 for Subtraction\n")
        print("Press 3 for Multiplication\n")
        print("Press 4 for Division\n")
        l=int(input("Level: "))
    return l
        
def generate_integer(l):
    global score
    p=random.randint(1,10)
    q=random.randint(1,10)
    if l==1:
        i=int(input(f"{p}+{q}= "))
        o=p+q
        if (o==i):
            score+=1
        
        if(o!=i):
            for _ in range(3):
                print("EEE")
                i=int(input(f"{p}+{q}= "))
            print("Correct Answer: ",o)
    
    elif l==2:
        if(p>q):
            i=int(input(f"{p}-{q}= "))
            o=p-q
        else:
            i=int(input(f"{q}-{p}= "))
            o=q-p
        if(o==i):
            score+=1
        if(o!=i):
            for _ in range(3):
                print("EEE")
                if(p>q):
                    i=int(input(f"{p}-{q}= "))
                else:
                    i=int(input(f"{q}-{p}= "))
            print("Correct Answer: ",o)
    
    elif l==3:
        i=int(input(f"{p}X{q}= "))
        o=p*q
        if(o==i):
            score+=1
        if(o!=i):
            for _ in range(3):
                print("EEE")
                i=int(input(f"{p}X{q}= "))
            print("Correct Answer: ",o)
       
    elif l==4:
        if(q!=0):
            i=float(input(f"{p}/{q}= "))
            o=p/q
        else:
            i=float(input(f"{p}/{1}="))
            o=p
        if(o==i):
            score+=1
        if(o!=i):
            for _ in range(3):
                print("EEE")
                i=float(input(f"{p}/{q}= "))
            print("Correct Answer: ",o)   

if __name__=="__main__":
    main()






