#reverse String through stack

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self,val):
        newNode = Node(val)
        if not self.top or self.length == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length +=1
        return self
    
    def pop(self):
        if not self.top or self.length == 0:
            return None
        temp = self.top 
        if self.length == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.length-= 1
        return temp
    
    def reverseString(self,string):
        reversedString = ""
        for char in string:
            self.push(char)
        while self.length > 0:
            reversedString+=str(self.pop().val)
            
        return reversedString
            
        
tt = None
    

