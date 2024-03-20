class DeQueue:
    def __init__(self,maxsize):
        self.dqueue = []
        self.front = -1
        self.back = -1
        self.size = 0
        self.maxSize = maxsize
    
    def addFront (self,data):
        if self.front == 0 :
            return print("dqueue is overflowed !!")
        elif self.front == -1 and self.back == -1 :
            self.front = self.front+1
            self.back = self.back+1
            self.dqueue.insert(self.front,data)
            self.size = self.size + 1
        else:
            self.front = self.front-1
            self.dqueue.insert(self.front,data)
            self.size = self.size + 1
            
    def deleteFront (self):
        if self.front == -1 and self.back == -1 :
            return print("dqueue is underFlowed !!")
        elif self.front > self.back :
            self.front == self.back == -1
        else :
            self.front = self.front + 1
            self.size = self.size - 1
            
    def addRear (self,data):
        if self.front == -1 and self.back == -1:
            self.front = self.front + 1
            self.back = self.back + 1
            self.dqueue.insert(self.back,data)
            self.size = self.size + 1
        elif self.back < self.maxSize :
            self.back = self.back + 1
            self.dqueue.insert(self.back,data)
            self.size = self.size + 1
        else:
            return print("dqueue is overflowed!")
        
    def deleteRear (self):
        if self.front == -1 and self.back == -1 :
            return print("dqueue is underFlowed!")
        elif self.back < self.front :
            self.front = self.back = -1
        else:
            self.back = self.back - 1
            self.size = self.size -1
            
    def Front (self):
        return print(self.dqueue[self.front])
    
    def isEmpty (self):
        if self.dqueue == []:
            return print("TRUE")
        else:
            return print("FALSE")
        
    def isFull (self):
        if self.size > self.maxSize :
            return print("FALSE")
        else:
            return print("TRUE")
    
    def sizeOfDqueue (self):
        return print("size of the DeQueue:-",self.size)
    
    def MaxSize (self):
        return print("maxsize of the Dequeue:-",self.maxSize)
    
    def display(self):
        if self.front == -1 and self.back == -1 :
            return print("DeQueue is Empty Nothing to Show !!")
        else:
            print("front:-",self.front," ","back:-",self.back)
            for i in range(self.front,self.back+1):
                print(self.dqueue[i])
    
newDeQueue = DeQueue(5)
    
newDeQueue.addFront(23)
newDeQueue.addFront(22)
newDeQueue.Front()
newDeQueue.display()
newDeQueue.addRear(22)
newDeQueue.deleteFront()
newDeQueue.Front()
newDeQueue.addFront(25)
newDeQueue.display()
    