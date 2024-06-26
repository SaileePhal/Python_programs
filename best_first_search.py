from queue import PriorityQueue

def best_first_search(graph,start,goal,heuristic):
    queue=PriorityQueue()
    queue.put((heuristic[start],start))
    visited=set()
    while not queue.empty():
        _,current=queue.get()
        if current==goal:
            return True

        visited.add(current)

        for i in graph[current]:
            if i not in visited:
                queue.put((heuristic[i],i))
    return False


graph={}
no_vertices=int(input("Enter no of vertices: "))
for i in range(no_vertices):
    node=input("enter node values: ")
    edges=input("enter edges: ").split()
    graph[node]=edges

heuristic={}
for i in range(no_vertices):
    node=input("enter node values: ")
    heuristic_val=input("enter heuristic value: ").split()
    heuristic[node]=heuristic_val

start_node=input("enter root node: ")
goal_node=input("enter goal node: ")

result=best_first_search(graph,start_node,goal_node,heuristic)

if result:
    print("Goal reached")
else:
    print("No solution found")

