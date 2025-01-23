class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Creating linked nodes
first = Node("Subscribe")
first.next = Node("to")
first.next.next = Node("Drop X Out")

