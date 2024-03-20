class Queue :
    
    def __init__(self,MAXSIZE):
        self.queue = []
        self.front = -1
        self.back = -1
        self.size = 0
        self.maxSize = MAXSIZE
        
    def Enqueue (self,data):
        if self.front == -1 and self.back == -1 :
            self.front = self.back = 0
            self.queue.insert(self.back,data)
            self.size = self.size+1
        elif self.size < self.maxSize:
            self.back = self.back+1
            self.queue.insert(self.back,data)
            self.size = self.size+1
        else:
            return print("stack is overflowed !!")
            
    def Dequeue (self):
        if self.front > self.back :
            self.front = self.back = -1
            
            return print("queue is underFlowed ")
        else :
            # self.queue.pop()
            self.front = self.front+1
            self.size = self.size-1
            
    def Front (self):
        if self.front == -1 and self.back == -1 or self.front > self.back :
            return print("queue is empty!")
        else:
            print(self.front)
            return print(self.queue[self.front])
    
    def isEmpty (self):
        if self.front == -1 and self.back == -1 or self.front > self.back :
            return print("queue is empty")
        else:
            return False
        
    def display (self):
        # print("self.front",self.front)
        # print("self.back",self.back)
        if self.front == -1 and self.back ==-1:
            return print("Queue is empty !!")
        for i in range(self.front,self.back+1):
           print(self.queue[i])
    
    def sizeOfQueue(self):
        return print("self of the queue:-",self.size)
    
    def maxSizeOfQueue(self):
        return print("max size of the queue:-",self.maxSize)
            
new_Queue = Queue(5)

new_Queue.Enqueue(2)
new_Queue.Enqueue(5)
new_Queue.Enqueue(23)
new_Queue.Enqueue(24)
new_Queue.Enqueue(12)

new_Queue.display()

new_Queue.Dequeue()
new_Queue.Dequeue()
new_Queue.Dequeue()
new_Queue.Dequeue()
new_Queue.Dequeue()
new_Queue.Dequeue()
new_Queue.display()

new_Queue.Front()

new_Queue.Enqueue(55)
new_Queue.Enqueue(28)
new_Queue.display()
new_Queue.Front()
new_Queue.sizeOfQueue()
new_Queue.maxSizeOfQueue()
