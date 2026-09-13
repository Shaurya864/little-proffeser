import twitter
def main():
    s=input("Enter the statement : ")
    shorten(s)
    
def shorten(s):
    v="A,E,I,O,U,a,e,i,o,u"
    c=""
    for i in s:
        if i not in v:
            c=c+i
    print("Output: ", c)

if __name__=="__main__":
    main()



