def BFS(node,graph):
   queue.append(node)          # add to queue
   while len(queue)!=0:
       x=queue.pop(0)          #pop first element
       if x not in visited:
           visited.add(x)     # add to visited list
           print(x)
           for i in graph[x]:       #acess vertex
               queue.append(i)




graph={}
num_vertices=int(input("Enter number of vertices:"))  #vertices
for i in range(num_vertices):                        # adding to graph
   vertex=input("Enter the vertex:")                #vertex -string
   edges=input("Enter the edges: ").split()           #edges -write in one line
   graph[vertex]=edges                              #accessing graph
   print(graph)


queue=[]                                   # queue implemntation
visited=set()     #root node
while(True):
    start=input("Enter the starting node: ")
    if start in graph:
        break
print("BFS traversal is: ")
BFS(start,graph)
