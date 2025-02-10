# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # Creating linked nodes
# first = Node("Subscribe")
# first.next = Node("to")
# first.next.next = Node("Drop X Out")


# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
        
# class SinglyLinkedList:
#     def __init__(self,val):
#         new_node = Node(val)
#         self.head = new_node
#         self.tail = self.head
#         self.length = 1
        
# #creating the linked list with an initial value
# first = SinglyLinkedList(10)
        
        
#PUSH MEHTHOD
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self,val):
        newNode = Node(val)
        self.head = newNode
        self.tail = self.head
        self.length = 1
 #push method   
    def push(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1
        return self
   #pop method
    def pop(self):
        if not self.head:
            return None
        temp = self.head
        pre = self.head
       
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    
    #unshift method
    def unshift(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length+=1
        return self
    
    #shift method
    def shift(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    #get method
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        i=0
        while i<index:
            temp = temp.next
            i+=1
        return temp
    #set method    
    def set(self,index,val):
        temp = self.get(index)
        if temp:
            temp.val = val
            return True
        else:
            return False
    #insert method     
    def insert(self,index,val):
        if index==0:
            return self.unshift(val)
        if index==self.length:
            return self.push(val)
        if index<0 or index>self.length:
            return None
        newNode = Node(val)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length+=1
        return self
    
    #remove method
    def remove(self,index):
        if index == 0:
            return self.shift()
        if index == self.length-1:
            return self.pop()
        if index<0 or index>=self.length:
            return None
        
        before = self.get(index - 1)  # Get the node before the one to be removed
        temp = before.next  # Node to be removed

        before.next = temp.next  # Bypass the node to be removed
        temp.next = None  # Disconnect it
        self.length -= 1  

        return temp     
    
    # #reverse method
    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp 
    #     next = temp.next 
    #     prev = None
        
    #     i=0
    #     while(i<self.length):
    #         next = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = next 
    #         i+=1
    #     return self
    
    #find middle
    def findMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    # def removeDuplicates(self):
    #     temp = self.head
    #     i = 0
    #     while temp.next:
    #         if temp.val == temp.next.val:
    #             return self.remove(i)
    #         temp = temp.next
    #         i+=1
    #     return None
    
    #remove duplicates in sorted list
    def removeDuplicates(self):
        current = self.head
        while current!=None and current.next!=None:
            if current.val == current.next.val:
                current.next = current.next.next
                self.length -=1
            else:
                current = current.next 
        return self
    
    #remove unsorted linked list
    def removeUnsortedDuplicates(self):
        if not self.head:
            return None
        uniqueValues = set()          
        current = self.head
        prev = None
        
        while current:
            if current.val in uniqueValues:
                prev.next = current.next
                self.length-=1
            else:
                uniqueValues.add(current.val)
                prev = current
            current=current.next
            
        self.tail = prev
        return self
    
    #detectCycleStart
    def detectCycleStart(self):
        slow = self.head
        fast = self.head
        #find loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None #agar loop nhi mila
        
        #finding starting point
        entry = self.head
        while slow!=entry:
            entry = entry.next
            slow = slow.next
        return slow
        
    
    
            
#creating object....  
first = SinglyLinkedList(0)
first.push(1)  
first.push(2)
first.push(3)
first.push(4)
first.push(3)
first.push(4)
# first.tail.next = first.head
# first.pop()
# first.unshift(13)
# first.unshift(10)
# first.shift()
# first.get(2)
# first.set(2,100)
# first.insert(0,10)
# first.insert(4,12)
# first.insert(2,15)
# first.remove(2)
# first.reverse()
first.findMiddle()
            
            
        