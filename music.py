import inflect
def main():
    p=inflect.engine()
    names=[]
    try:
        while(1):
            name=input("Name: ")
            names.append(name)
    except EOFError:
        print()
    format=p.join(names)
    print(f"Adieu, adieu, to {format}")
main()
        
