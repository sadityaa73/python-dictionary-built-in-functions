# creating a class for Node of a List:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class List:
    
    def __init__(self):
        self.head = None
        
    def push(self,data):
        new_Node = Node(data)
        
        if self.head is None:
            self.head = new_Node
            return
        else:
            self.currentNode = self.head
            while self.currentNode.next is not None:
                self.currentNode = self.currentNode.next
            self.currentNode.next = new_Node
            
    def pop(self):
        tempNode = self.head
        while tempNode is not None:
            if tempNode.next.next is None:
                tempNode.next = None
            tempNode = tempNode.next

    def display(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.data,end='->')
            if tempNode.next is None:
                print("NULL")
            tempNode = tempNode.next
        
        
l1 = List()
l1.push(2)
l1.push(12)
l1.push(32)
l1.push(4)
l1.push(5)
l1.display()
l1.pop()
print("after poping element from the stack")
l1.display()



        
        
    