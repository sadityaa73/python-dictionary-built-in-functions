# implemting stack using LIFOQUEUE module:

from queue import LifoQueue

stack = LifoQueue(maxsize=5)

# creating a funciton to insert element into stack:

def insert(value):
    if stack.full():
        print("stack is overFlowed")
    else:
        stack.put(value)
        
# creating function to delete elements from the stack:

def delete():
    if stack.empty():
        print("stack is underFlow")
    else:
        stack.get()
        
#creating a function to check the size of the stack :

def queue_size():
    print(stack.qsize())
    
    
# calling stack funciton:

insert(2)
insert(6)
insert(3)
insert(12)
insert(6)

queue_size()

delete()


queue_size()

