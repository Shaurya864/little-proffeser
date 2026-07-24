while(1):
    try:
        s=input("Fraction: ")
        s=s.split("/")
        x=int(s[0])
        y=int(s[1])
        c=x/y 
        c=c*100
        if c>=99:
            print("F")
        elif c==0:
            print("E")
        else:
            print(f"{c}%")
        break

    except ValueError:
        continue
    except ZeroDivisionError:
        continue

