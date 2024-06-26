def DFS(visited,graph,node):
   if node not in visited:
       print(node)
       visited.add(node)
       for i in graph[node]:
           DFS(visited,graph,i)

graph={}
num_vertices=int(input("Enter number of vertices: "))  #vertices
for i in range(num_vertices):                        # adding to graph
   vertex=input("Enter the vertex: ")                #vertex -string
   edges=input("Enter the edges: ").split()           #edges -write in one line
   graph[vertex]=edges                              #accessing graph
   print(graph)


visited=set()                              #root node
while(True):
    start=input("Enter the starting node: ")
    if start in graph:
        break
print("DFS traversal is: ")
DFS(visited,graph,start)
