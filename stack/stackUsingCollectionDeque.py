# implementing stack using collection dqeue:

from collections import deque

stack = deque()
maxsize = 5
#creating a funciton to insert element into the stack:

def insert(value):
    if len(stack) < maxsize :
        stack.append(value)
    else :
        print("stack is overFlowed")
        
# creating a function to delete element from the stack:

def delete():
    if len(stack)<=0 :
        print("stack is underFlowed")
    else:
        stack.pop()
        
# creating a funciton to print the elements are in stack:

def elements():
    print(stack)
# calling stack function:

insert(1)
insert(4)
insert(10)
elements()
insert(14)
elements()
delete()
elements()
delete()
elements()
     
