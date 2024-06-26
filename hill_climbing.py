def hill(node,count,prev_heuristic):
    if len(_open)!=0:
        current=_open.pop(0)
        closed.append(current)

    if current==goal:
        print("Hill Climbing Path ",closed[0],end="")
        for i in closed[1:]:
            print(" - > ", i,end="")
        return

    elif heuristic[current]>prev_heuristic:
        print("Goal node not reached")
        return

    else:
        for i in graph[current]:
            if i not in closed and i not in _open:
                _open.append(i)
                count+=1

        _open.sort(key=lambda  x: heuristic[x])
        hill(_open[0],count,heuristic[current])

def adjacent(node):
    graph[node]=input("Enter child node "+node+" : ").split()
    for i in graph[node]:
        if i not in graph:
            adjacent(i)




_open=[]
closed=[]
count=0

graph={}
root=input("Enter node: ")
adjacent(root) #function to input in graph without no of vertices

heuristic={}
for j in graph:
    heuristic[j]=float(input("Enter heuristic value "+j+" : "))

start=input("Enter root node: ")
goal=input("Enter goal node: ")

_open.append(start)
prev_heuristic=heuristic[start]     #stores previous value for comparison later
hill(start,count,prev_heuristic)
