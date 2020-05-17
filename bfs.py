#BFS algorithm 
#1. Input a graph object containing all vertices and edges
#2. A vertex id repersenting the source
#Returns a list of vertices ids in the order they were visited

def BFS(Graph,vertexID):
    
    #Queue
    queue = [vertexID]
    #Keep track of the vertices of the graph visited
    visitingOrder = []
    
    #Getting the adjacency list
    adjacency = Graph.get_adjacency_list()
    newGraph = adjacency[1]
    
    #While Q is not empty
    while len(queue) > 0:
        #deqeue
        currVer = queue.pop(0)
     
        #if the vertext is not yet visited
        if currVer not in visitingOrder:
            #the vertex is discovered
            visitingOrder.append(currVer)
            nVertex = newGraph[currVer]
            
            for Vertex in nVertex:
                queue.append(Vertex)
                
    #return the path taken to get to vertexID            
    return visitingOrder