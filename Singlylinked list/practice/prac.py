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
    
#     def count(self):
#         if not self.head:
#             return None
#         temp = self.head
#         count = 0
#         while temp:
#             count+=1
#             temp = temp.next
#         return count
    
# tt= None
            
            
#11
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next=  None

# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length  = 1
#     def push(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         self.tail.next = newNode
#         self.tail = newNode
#         self.length+=1
#         return self
    
#     def search(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp = self.head
#         i = 0
#         while i<index:
#             temp = temp.next
#             i+=1
#         return temp.val
    
# tt = None
        
        
#12
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
#         self.tail.next = newNode
#         self.tail = newNode
#         self.length+=1
#         return self
    
#     def reverse(self):
#         if not self.head:
#             return None
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#         next = temp.next
#         prev = None
#         i = 0
#         while i<self.length:
#             next = temp.next
#             temp.next = prev
#             prev = temp
#             temp = next
#             i+=1
#         return self
    
# tt = None

#13
# class Node:
#     def __init__(self,val):
#         self.val = val 
#         self.next = None
        
# class Singly:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.length = 0
        
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
    
#     def pop(self):
#         if not self.head:
#             return None
#         pre = self.head 
#         temp  =self.head
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
    
#     def isEmpty(self):
#         if not self.head and not self.tail:
#             return "empty"
#         else:
#             return "not empty"
    
# tt = None

#14
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
#         self.length +=1
#         return self
    
#     def get(self,index):
#         if index<0 or index>self.length:
#             return None
#         i=1
#         temp = self.head
#         while i<index:
#             temp = temp.next
#             i+=1
#         return temp.val
    
#     def printReverse(self):
#         i= self.length
#         while i>0:
#             print(self.get(i),end="-->")
#             i-=1
#         print("none")
        
# tt = None        
         

#15
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
    
#     def findMiddle(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
    
# tt = None
            

#16
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
    
#     def detectLoop(self):
#         if not self.head:
#             return None
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return "loop" 
            
#         else:
#             return "not loop"
                     
# tt = None
   
#17
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
#         self.length +=1
#         return self
    
#     def removeLoop(self):
#         if not self.head:
#             return None
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow==fast:
#                 print("loop")
#                 break
#         else:
#             return " no loop"
        
#         self.tail.next = None
#         return self
        
# tt = None


#20
#sorted linked list
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
    
# class Singly:
#     def __init__(self,val):
#         newNode = Node(val)
#         self.head = newNode
#         self.tail = self.head
#         self.length  = 1
        
#     def push(self,val):
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#             self.tail = self.head
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length +=1
#         return self
    
#     def removeSortedDuplicate(self):
#         if not self.head:
#             return None
#         temp = self.head
#         while temp and temp.next:
#             if temp.val == temp.next.val:
#                 temp.next = temp.next.next
#                 self.length -=1
#             else:
#                 temp = temp.next
#         return self
    
#     def removeUnsortedDuplicate(self):
#         if not self.head:
#             return None
#         temp = self.head
#         prev = None
#         storeSet = set()
#         while temp:
#             if temp.val in storeSet:
#                 prev.next = temp.next
#                 self.length-=1
#             else:
#                 storeSet.add(temp.val)
#                 prev = temp
#             temp = temp.next
#         self.tail = prev
#         return self
    
# tt = None
    
    
    
    
#22
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
    
#     def get(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp = self.head
#         i= 0
#         while i<index:
#             temp = temp.next
#             i+=1
#         return temp
    
    
#     def swap(self,index1,index2):
#         if index1<0 or index1>=self.length or index2<0 or index2>=self.length:
#             return None
#         a = self.get(index1)
#         b = self.get(index2)
        
#         if a.val == b.val:
#             return None
#         else:
#             temp = b.val
#             b.val = a.val
#             a.val = temp
#         return self
            
        
    
# tt = None
         

        
        
    
