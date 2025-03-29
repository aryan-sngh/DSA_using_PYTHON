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
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacencyList and vertex2 in self.adjacencyList:
            if vertex1 in self.adjacencyList[vertex2]:
                self.adjacencyList[vertex2].remove(vertex1)
            if vertex2 in self.adjacencyList[vertex1]:
                self.adjacencyList[vertex1].remove(vertex2)
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex not in self.adjacencyList:
            return None
        while self.adjacencyList[vertex]:
            temp = self.adjacencyList[vertex].pop()
            self.removeEdge(vertex,temp)
            
        del self.adjacencyList[vertex]
        return self
            
            
    
tt = None
    
    
    
        