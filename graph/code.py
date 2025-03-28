class Graph:
    def __init__(self):
        self.adjacencyList = {}
        
    
    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []
            return True
        return False
    
    def addEgde(self,vertex1,vertex2):
        if vertex1 in self.adjacencyList and vertex2 in self.adjacencyList:
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return True
        return False
    
tt = None
    
    
    
        