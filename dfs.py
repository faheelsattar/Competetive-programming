def dfs(graph, start, visited):    
    if start in visited:
        return
    visited.append(start)
    print(start)
    for node in graph[start]:
        dfs(graph, node, visited)
                 
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
visited=[]
dfs(graph, start, visited)