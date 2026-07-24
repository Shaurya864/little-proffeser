try:
    total=0
    while(1):
        x=int(input("enter score: "))
        total+=x
except EOFError:
    print("score is :",total)