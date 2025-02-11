#3
# class Node:
#     def __init__(self,val):
#         self.val = val #store data
#         self.next = None #pointer to next
        
# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
    
#     def append(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length+=1
#         return self
    
#     def traverse(self):
#         temp = self.head
#         while temp:
#             print(temp.val,end="-->")
#             temp = temp.next
#         print("None")
        
# first = Singly(0)
# first.append(1)
# first.append(2)
# first.traverse()


#4
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
# class singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode 
#         self.tail = self.head
#         self.length = 1
        
#     def beginning(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         newNode.next = self.head
#         self.head = newNode
#         self.length+=1
#         return self
    
# first = singly(0)
# first.beginning(1)

#5
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
        
# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
    
#     def end(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length+=1
#         return self
             
# tt = Singly(0)
# tt.end(1)


#6
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
        
#     def end(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head 
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length+=1
#         return self

#     def beginning(self,val):
#         newNode = Node(val)
#         newNode.next = self.head
#         self.head = newNode
#         self.length+=1
#         return self
    
#     def get(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp = self.head
#         i = 0
#         while i<index:
#             temp = temp.next
#             i+=1
#         return temp
    
#     def insert(self,index,val):
#         if index==0:
#             return self.beginning(val)
#         if index==self.length:
#             return self.end(val)
#         if index<0 or index>self.length:
#             return None
#         newNode = Node(val)
#         temp = self.get(index-1)
#         newNode.next = temp.next
#         temp.next = newNode
#         self.length+=1
#         return temp

# tt = Singly(0)

#7
# class Node:
#     def __init__(self,val):
#         self.val = val 
#         self.next = None
# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
        
#     def push(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length+=1
#         return self
    
#     def firstDelete(self):
#         if not self.head:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length-=1
#         if self.length==0:
#             self.head = None
#             self.tail = None
#         return temp
    
# tt = Singly(0)
        
#8
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
    
#     def push(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next= newNode
#             self.tail = newNode
#         self.length+=1
#         return self
    
#     def lastdelete(self):
#         if not self.head:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length-=1
#         if self.length==0:
#             self.head = None
#             self.tail = None
#         return temp
            
# tt = Singly(0) 

#9
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length = 1
    
#     def push(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length+=1
#         return self
    
    
#     def deleteEnd(self):
#         if not self.head:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length-=1
#         if self.length==0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def deleteStart(self):
#         if not self.head:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length-=1
#         if self.length==0:
#             self.head = None
#             self.tail = None
#         return temp
    
#     def get(self,index):
#         if index<0 or index>= self.length:
#             return None
#         temp = self.head
#         i= 0
#         while i<index:
#             temp = temp.next
#             i+=1
#         return temp
    
#     def remove(self,index):
#         if index ==0:
#             return self.deleteStart()
#         if index==self.length-1:
#             return self.deleteEnd()
#         if index<0 or index>=self.length:
#             return None
#         before = self.get(index-1)
#         temp = before.next
#         before.next = temp.next
#         temp.next = None
#         self.length-=1
#         if self.length==0:
#             self.head = None
#             self.tail = None
#         return temp
    
# tt = None
        
        
#10
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singly:
    def __init__(self,val):
        newNode = Node(val)
        self.head = newNode
        self.tail = self.head 
        self.length = 1
        
    def push(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length+=1
        return self
    
    def count(self):
        if not self.head:
            return None
            
        
            
    
           

        