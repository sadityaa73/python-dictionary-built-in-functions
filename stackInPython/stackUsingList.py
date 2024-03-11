# implementing stack data structure in python using list[].

#creating a stack using list;

stack = list()

#careting a function for append element to the stack:

def push(value):
    if len(stack) < 6 :
        stack.append(value)
    else :
        print("Stack is overFlowed")
        return
        
#creating a function to pop the element from the stack

def pop():
    if len(stack) <=0 :
        print("stack is underFlowed")
    else :
         print("current item to be poped from the stack is :- ",stack[0])
         stack.pop(0)
    
# creating a function for view elements that are present inside the stack:

def elements():
    print("elements of the stack:")
    print(stack)

# creating a function know peek element of the stack:

def peek():
    print("top of the stack : ",stack[0])
    
    
# calling stack function

push(2)
push(12)
push(6)
peek()
elements()
print("\n")
print("after deleteing elements from the stack:")
print("\n")
pop()
peek()
elements()
push(12)
push(12)
push(1)
push(4)
elements()
push(1)
push(4)
elements()
