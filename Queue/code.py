class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class Queue:
    def __init__(self,val):
        newNode = Node(val)
        self.first = newNode
        self.last = self.first
        self.length = 1
        
    def enqueue(self,val):
        newNode = Node(val)
        if self.length == 0:
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = newNode
        self.length +=1
        return self
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next 
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return self
    
tt = None
        
            
        
        
        