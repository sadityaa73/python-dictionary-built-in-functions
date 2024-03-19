# create a Node Class :
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
#Create a List Calss:

class List:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        else:
            self.currentNode = self.head
            while self.currentNode.next != None:
                self.currentNode = self.currentNode.next
            self.currentNode.next = new_Node
    
    def pop(self):
        temp = self.head
        while temp is not None:
            if temp.next.next is None:
                temp.next = None
            temp = temp.next
            
                
    def display(self):
        tempNode = self.head
        print("[")
        while tempNode != None :
            print(tempNode.data,end='->')
            if tempNode.next is None :
                print("NULL")
            tempNode = tempNode.next
        print("]")   
            
l1 = List()
l1.insert(21)
l1.insert(2)
l1.insert(24)
l1.insert(32)
l1.display()
l1.pop()
print("print list after poping",end='\n')
l1.display()