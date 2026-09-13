class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverseprint(head):
    
    while head:
        print(head.data,end="->")
        head=head.next
    print("null")
def lowest(head):
    min=head.data
    currentnode=head.next
    while currentnode:
        if currentnode.data<min:
            min=currentnode.data
        currentnode=currentnode.next
    return min
def deletespecific(head,nodetodelete):
    if head==nodetodelete:
        return head.next
    currentnode=head
    while currentnode.next and currentnode.next!=nodetodelete:
        currentnode=currentnode.next
    if currentnode.next is None:
        return head
    currentnode.next=currentnode.next.next
    return head
def insert(head,newnode,position):
    if position==1:
        newnode.next=head
        return newnode
    currentnode=head
    for _ in range(position - 2):
        if currentnode is None:
            break
        currentnode=currentnode.next
    newnode.next=currentnode.next
    currentnode.next=newnode
    return head 


node1=node(7)
node2=node(11)
node3=node(3)
node4=node(2)
node5=node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

traverseprint(node1)
print("Lowest Value is : ",lowest(node1))
node1=deletespecific(node1,node4)
traverseprint(node1)
newNode=node(97)
node1=insert(node1,newNode,2)
traverseprint(node1)
