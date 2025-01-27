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
first  = SinglyLinkedList(20)
first.push(25)  
first.push(24)
first.push(22)
            
            
            
        