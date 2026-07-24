def main():
    items={
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }
    total=0
    try:
        while(1):
            item=input("Item: ").lower()
            total+=items[item]
    except EOFError:
        print(f"Total:${total}")
if __name__=="__main__":
    main()

