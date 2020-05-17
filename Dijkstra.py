#Follows the algorithm/psuedocode from Wikipedia
#Input the graph, the initial vertex, and the end vertex
#Outputs a tuple of size 2: 1: contains the ids of the vertices, 2: the distance
def shortest_path(graph,src_id,dest_id):
    
    #Getting the adjacency list of the graph
    nGraph = graph.get_adjacency_list()
    Graph = nGraph[1]
    nodes = nGraph[0]
    #Mark all nodes as unvisited (create a set containing all vertices)
    vertexSet = nodes
    
    #Empty set containing the distances between two vertices
    distance = {}
    
    #Contaning the adjacent nodes of the vertices (for getting path)
    previous = {}
    
    #for vertex v in graph
    for v in Graph:
        #Set all distances to infinity
        distance[v] = float('inf')
        #set the adjacent nodes to none/undefined (for path)
        previous[v] = None
        
    #Set initial vertex distance to 0
    distance[src_id] = 0
    
    #While the vertex set is not empty
    while len(vertexSet) > 0:
        
        #Getting the minimum distance
        
        minVertex = vertexSet[0]
        
        minDistance = distance[minVertex]
        
        #Only vertex which are still in the vertex set
        for n in range(1,len(vertexSet)):
            
            if distance[vertexSet[n]] < minDistance:
                minVertex = vertexSet[n]
                minDistance = distance[minVertex]
                
                
                
        u = minVertex
        
        
        #remove u from the set (the current node)
        vertexSet.remove(u)
        
        #Terminate search if src_id = dest_id (u = target)
        if (u == dest_id):
            break
        
        #only v that is still in the vertex set
        for i in Graph[u]:
            alternate = Graph[u][i] + distance[u]
            if distance[i] > alternate:
                distance[i] = alternate
                previous[i] = u
   


    #Get the path taken for the shortest distance
    vertexID = dest_id
    path2 = []
    path2.append(dest_id)
    while src_id not in path2:
             vertexID = (previous[vertexID])
             path2.append(vertexID)
    path2.reverse()
    
    #Return the path and the distance
    return path2, distance[dest_id]

