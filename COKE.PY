amount=50
coin=[25,10,5]
print("Amount Due: ",amount)
while(1):
    while(amount!=0 and amount>0):
        coins=int(input("Insert Coin: " ))
        if coins in coin:
             amount=amount-coins
        if amount>0:
             print("Amount Due: ",amount)
        if (amount<=0):  
            print("Changed Owed: ",amount*-1)
    break    
