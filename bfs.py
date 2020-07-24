def bfs(graph, start):
    q= []
    visited=[]
    q.append(start)
    visited.append(start)
    while q:
        start=q.pop(0)
        print(start, end = " ")
        for neighbour in graph[start]:
          if neighbour not in visited:
            visited.append(neighbour)
            q.append(neighbour)
        
                
graph={ }
n = int(input("Length of graph"))
for i in range(0,n):
    key = input("Enter the node")
    val = input("Enter the adjacent node to it")
    if key in graph:
        graph[key].append(val)
    else:   
        graph[key]=[]
        graph[key].append(val)

start= input("Specify a starting node")

bfs(graph, start)
