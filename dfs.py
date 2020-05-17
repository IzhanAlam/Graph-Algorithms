def DFS(Graph,vertexID):
    
    #Stack, set vertexID
    stack = [vertexID]
    
    #Path taken
    visitingOrder = []
    
    #adjacency list from the graph
    adjacency = Graph.get_adjacency_list()
    newGraph = adjacency[1]
    
    #While stack is not empty
    while len(stack) > 0:
        #remove the vertex from the stack
        vertex = stack.pop()
        
        #if vertex is not yet visited
        if vertex not in visitingOrder:
            #add it to visited
            visitingOrder.append(vertex)
        else:
            continue
        
        for nVertex in newGraph[vertex]:
            stack.append(nVertex)
            
    return visitingOrder