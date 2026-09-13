def main():
    s=input("Input :")
    c=""
    vowels="a,e,i,o,u,A,E,I,O,U"
    for i in s:
        if i not in vowels:
            c=c+i
    print("Output:",c)
main() 

