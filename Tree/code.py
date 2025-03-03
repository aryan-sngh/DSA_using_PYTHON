class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
        
    def insert(self,val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return self
        
        temp = self.root
        while True:
            if newNode.val == temp.val:
                return None
            if newNode.val < temp.val:
                if temp.left is None:
                    temp.left = newNode
                    return self
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return self
                else:
                    temp = temp.right 
                    
    def find(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value <temp.val:
                temp = temp.left
            elif value>temp.val:
                temp= temp.right
            else:
                return True
        else:
            return False
            
                
                
tt = None            

        