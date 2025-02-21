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
    
    def set(self,index,val):
        temp = self.get(index)
        if temp:
            temp.val = val
            return True
        else:
            return False
    
    def insert(self,index,val):
        if index == 0:
            return self.unshift(val)
        if index == self.length :
            return self.push(val)
        if index<0 or index>self.length:
            return None
        # newNode = Node(val)
        # temp = self.get(index-1)
        # newNode.next = temp.next
        # temp.next.prev = newNode
        # temp.next = newNode
        # newNode.prev = temp
        #or 
        newNode = Node(val)
        before = self.get(index-1)
        after = before.next
        before.next = newNode
        newNode.prev = before
        newNode.next = after
        after.prev = newNode
        self.length +=1
        return self
    
    def remove(self,index):
        if index == 0:
            return self.shift()
        if index == self.length -1:
            return self.pop()
        if index<0 or index>=self.length:
            return None
        before = self.get(index-1)
        after = before.next
        before.next = after.next
        after.next.prev = before
        after.next = None
        after.prev = None
        self.length-=1
        return self
    
    #swap first and last
    def swapFirstLast(self):
        if not self.head or self.length == 0 or self.length<2:
            return None
        
        
        first = self.head
        last = self.tail
        temp = None
        temp = first.val
        first.val = last.val
        last.val = temp
        return self
        
    def reverse(self):
        if not self.head or self.length == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        next = temp.next
        back = None
        i = 0
        while i<self.length:
            next = temp.next
            temp.next = back
            temp.prev = next
            back = temp
            temp = next
            i+=1
        return self
    
    def detectLoop(self):
        if not self.head or self.length== 0:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "loop"
        else:
            return None
        
    def isPalindrome(self):
        if not self.head or self.length == 0:
            return None
        forwardNode = self.head
        backwardNode = self.tail
        i = 0
        while i<self.length/2:
            if forwardNode.val != backwardNode.val:
                return False
            forwardNode = forwardNode.next
            backwardNode = backwardNode.prev
            i+=1
        return True
tt = None
        
        
        
        

 
        