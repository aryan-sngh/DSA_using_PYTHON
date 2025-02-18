#first node of doubly linked list
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None
        
# class DoublyLinkedList:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
        
# first = None


#lets create method
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self,val):
        newNode = Node(val)
        self.head = newNode
        self.tail = self.head
        self.length = 1
    
    #push mothod    
    def push(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail 
            self.tail = newNode
        self.length +=1
        return self
    
    
    def pop(self):
        if self.length==0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp 
    
    def unshift(self,val):
        newNode = Node(val)
        if not self.head or self.length ==0:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length+=1
        return self  
    
    def shift(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head  = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index<self.length/2:
            temp = self.head
            i=0 
            while i<index:
                temp = temp.next
                i+=1
        else:
            temp = self.tail 
            i = self.length-1
            while i>index:
                temp = temp.prev
                i-=1
        return temp
        
        
tt = None
        
        
        

 
        