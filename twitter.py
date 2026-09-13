s=input("Input : ")
c=" "
v="A,E,I,O,U,a,e,i,o,u"
for i in s:
    if i not in v:
        c=c+i
print("Output: ",c)
