class stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        self.stack.pop()
    def isempty(self):
        return not bool(self.stack)
    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)

#create a stack
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("INSERTED Stack is:",s)
s.pop()
print("New Stack After Poppinf one element: ",s)
print("Peek element",s.peek())
print("isempty:",s.isempty())

    