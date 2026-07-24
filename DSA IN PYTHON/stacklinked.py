class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class stack:
    def __init__ (self):
        self.head=None
        self.size=0
    def push(self,value):
        new=node(value)
        if self.head:
            new.next=self.head
        self.head=new
        self.size+=1
    def pop(self):
        if self.isempty():
            return"Stack is Empty"
        popped=self.head
        self.head=self.head.next
        self.size-=1
        return popped.value
    

