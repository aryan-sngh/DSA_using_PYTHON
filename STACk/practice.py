#reverse String through stack

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
#         self.length = 0
    
#     def push(self,val):
#         newNode = Node(val)
#         if not self.top or self.length == 0:
#             self.top = newNode
#         else:
#             newNode.next = self.top
#             self.top = newNode
#         self.length +=1
#         return self
    
#     def pop(self):
#         if not self.top or self.length == 0:
#             return None
#         temp = self.top 
#         if self.length == 1:
#             self.top = None
#         else:
#             self.top = self.top.next
#             temp.next = None
#         self.length-= 1
#         return temp
    
#     def reverseString(self,string):
#         stack = Stack()
#         reversedString = ""
#         for char in string:
#             stack.push(char)
#         while stack.length > 0:
#             reversedString+=str(stack.pop().val)
            
#         return reversedString
    
#     def isBalancedParanthesies(self,s):
#         stack = []        
#         openingBrackets = ['(','{','[']
#         closingBrackets = [')','}',']']
#         for char in s:
#             if char in openingBrackets:
#                 stack.append(char)
#             elif char in closingBrackets:
#                 if not stack:
#                     return False
#                 lastOpenedBracket = stack.pop()
#                 matchingOpeningBrakcet = openingBrackets[closingBrackets.index(char)]
#                 if matchingOpeningBrakcet != lastOpenedBracket:
#                     return False
#         return len(stack) == 0
    
            
        
# tt = None


class StackList:
    def __init__(self):
        self.items = []
        
    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        if len(self.items) == 0:
            return False
        return self.items.pop()
        
def sortedList(stack):
    tempStack = StackList()
    
    while len(stack.items) > 0:
        current = stack.pop()
        
        while len(tempStack.items) > 0 and tempStack.items[-1] > current:
            stack.push(tempStack.pop())
        
        tempStack.push(current)
        
    while len(tempStack.items) > 0:
        stack.push(tempStack.pop()) 
    
    return stack   
        
s = StackList()
s.push(6)
s.push(2)
s.push(-5)
s.push(1)
s.push(5)

sortedList(s)




        
    