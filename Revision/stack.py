
class Stack:
    
    def __init__(self,size):
        self.list =[];
        self.size = size
        self.top = -1;
        
    def is_empty(self):
        if self.top == -1 or self.top <= self.size-2:
            return True;
        else:
            return False;
    def is_overflow(self):
        if self.top > self.size-2:
            return True;
        else:
            return False;
        
    def push(self,val):
        print("top",self.top,"size",self.size);
        if self.top > self.size-2:
            print("list is full please delete some item first");
        else:
            self.list.append(val);
            self.top += 1;
            
    
    def pop(self):
        if self.top == -1:
            return "list is empty add some item first";
        
        else:
            print("item to be poped",self.list[self.top]);
            self.list.pop();
            self.top -= 1;
            
    def display_stack(self):
        print(self.list);
s1 = Stack(5);
print("is_empty",s1.is_empty());
s1.push(2);
s1.push(12);
s1.push(24);
s1.push(28);
s1.push(22);
s1.display_stack();
print("is_overflow",s1.is_overflow());

