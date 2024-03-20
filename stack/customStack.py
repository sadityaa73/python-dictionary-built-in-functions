# stack has following operations:
# 1.push() 2.pop() 3.isEmpty() 4.peek/Top () 5.size()

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push (self,data):
        self.stack.append(data)
    
    def pop (self):
        if self.stack == [] :
           print("stack is empty")
           return
        else:
         elementBePoped = self.stack[len(self.stack)-1]
         self.stack.pop()
         return elementBePoped
         
        
    def isEmpty(self):
        if self.stack == [] :
            return True
        else:
            return False
        
    def top(self):
        if self.stack == [] :
            return -1
        else:
            return self.stack[len(self.stack)-1]
    
    def size(self):
        print(len(self.stack))
    
    def display(self):
        print(self.stack,end='\t')
        print(end="\n")

