class Queue():
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    def enqueue(self,data):
        if (self.tail == self.k - 1):
            print("queue is full")
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data
    def dequeue(self):
        if (self.head == -1):
            print("queue is empty")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1 
            return temp
    def printqueue(self):
        if (self.head == -1):
            print("no element exist")
        else:
            for i in range(self.head , self.tail + 1):
                print(self.queue[i], end= " ")
            print ()

obj = Queue(5)
obj.printqueue()
obj.dequeue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.printqueue()
obj.dequeue()
obj.printqueue()
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
obj.printqueue()
obj.enqueue(7)
obj.printqueue()

#this is comment 
#Why did it say full even though there was an empty spot?
#This is the main drawback of a Linear Queue. As you dequeue items, the head moves forward, leaving empty space behind it that can never be reused because the tail only moves in one direction.