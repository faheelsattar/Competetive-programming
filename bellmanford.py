def bellmanFord(graph, vert, src):
    dist = [float("Inf")] * vert 
    dist[src] = 0
    for _ in range(vert-1):
        for u,v,w in graph:
            if dist[u] != float("Inf") and dist[u] +w < dist[v]:
                dist[v] = dist[u] +w
    
    for u,v,w in graph:
            if dist[u] != float("Inf") and dist[u] +w < dist[v]:
                print("Graph contains negative weight cycle") 
                return  
    
    print(dist)




graph=[]

graph.append([0, 1, -1])
graph.append([0, 2, 4])
graph.append([1, 2, 3])
graph.append([1, 3, 2])
graph.append([1, 4, 2])
graph.append([3, 2, 5])
graph.append([3, 1, 1])
graph.append([4, 3, -3])

vert=5
src=0
bellmanFord(graph, vert, src)