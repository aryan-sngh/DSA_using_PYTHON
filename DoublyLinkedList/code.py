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
        
first = None
        
        