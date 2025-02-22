class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class Stack:
    def __init__(self,val):
        newNode = Node(val)
        self.top = newNode
        self.length = 1

first = None