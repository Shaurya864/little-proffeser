stack=[]
#push
stack.append('1')
stack.append('2')
stack.append('3')
#peek
top=stack[-1]
print("Peek: ",top)
#pop
print("Stack before pop :",stack)
popped=stack.pop()
print("pop:",popped)
print("Stack after pop :",stack)
#isempty
isempty=not bool(stack)
print("isempty:",isempty)
#size
print("size",len(stack))

