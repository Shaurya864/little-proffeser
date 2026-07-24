queue=[]
#enqueue
queue.append('1')
queue.append('2')
queue.append('3')
queue.append('4')
queue.append('5')
print("Given queue is ",queue)
#front and rear
print(f"Front element is {queue[0]} and rear is {queue[4]}")
#dequeue
queue.pop(0)
print("QUEUE AFTER POPPED :",queue)
#is empty
isempty=not bool(queue)
print("Is empty ",isempty)
#size
print("Size :",len(queue))