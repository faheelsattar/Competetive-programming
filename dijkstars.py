from queue import PriorityQueue
def dijkstra(graph, n, src):
    q= PriorityQueue()
    dist = [float("Inf")] * n 
    dist[src] = 0
    q.put((0, src))
    while not q.empty():
        a= q.get()[1]
        if str(a) in graph:   
            for node in graph[str(a)]:
                b= int(node[0])
                w= int(node[1])
                if dist[a]+w < dist[b]:
                    dist[b] = dist[a]+w
                    q.put((-dist[b],b))

    for i in range(0, len(dist)):
        print(i, dist[i])
         
graph={ }
n = int(input("Length of graph"))
for i in range(0,n):
    key = input("Enter the node")
    val = input("Enter the adjacent node to it")
    w= input("Enter weight for it")
    if key in graph:
        graph[key].append((val, w))
    else:   
        graph[key]=[]
        graph[key].append((val, w))

start= int(input("Specify a starting node"))
dijkstra(graph, n, start)
