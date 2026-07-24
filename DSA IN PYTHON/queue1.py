class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
         self.queue.append(element)
    def FR (self):
        print(f"front is {self.queue[0]} and rear is {self.queue[len(self.queue)-1]}")

    def dequeue(self):
        return self.queue.pop(0)
    def isempty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)

Q=queue()
size=int(input("Enter the size of queue you want:"))

for i in range(size):
    element=input("Enter element: ")
    Q.enqueue(element)
print("Queue you filled: ",Q)
print(Q.FR())
print("Size of queue is:",Q.size())
print("Is empty:",Q.isempty())

j=int(input("How you want the dequeue :"))
if j>size:
    print("cannot dequeue")
for y in range(j):
    Q.dequeue()
print("Queue you filled: ",Q)
print("Is empty:",Q.isempty())

if Q.isempty():
    print("Front and rear both are equal =-1")

else:
    print(Q.FR())
    print("Size of queue is:",Q.size())
