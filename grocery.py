def main():
    try:
        total=[]
        while(1):
            x=input().strip()
            total.append(x.upper())
        
    except EOFError:
        total.sort()
        for i in total:
            print(i)
if __name__=="__main__":
    main()
