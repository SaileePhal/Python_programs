from collections import deque
def BFS(a, b, target):
  visited = {}
  isSolvable = False    #Flag to chk if solution has reached
  path = []
  q = deque()
  q.append((0, 0))
  while (len(q) > 0):
    u = q.popleft()               # Pop the leftmost element
    if ((u[0], u[1]) in visited): # If node is already in visited then contimue
      continue

    path.append([u[0], u[1]])    # partial solution

    visited[(u[0], u[1])] = 1       # assign value of it as 1 to show that its visited

    if (u[0] == target or u[1] == target):
         isSolvable = True
         if(u[0] == target):
             if (u[1] != 0):
                 path.append([u[0], 0])
         else:
             if (u[0] != 0):
                 path.append([0, u[1]])
         l = len(path)
         for i in range(l):
             print("(", path[i][0], ",",path[i][1], ")")   #Print the solution
         break

    q.append([a, u[1]]) # Fill Jug1
    q.append([u[0], b]) # Fill Jug2
    x = min(u[1], (a-u[0]))
    y = min(u[0], (b-u[1]))
    q.append([u[0]+x,u[1]-x])  # Swap Jug1 from Jug2 to make Jug1 full
    q.append([u[0]-y,u[1]+y])  # Swap Jug2 from Jug1 to make Jug2 full
    q.append([0, b])   # Empty Jug1
    q.append([a, 0])   # Empty Jug2

  if not isSolvable:
    print("No solution exists")


a=int(input("Enter capacity of Jug1: "));
b=int(input("Enter capacity of Jug2: "));
c=int(input("Enter final capacity or target value: "));
Jug1, Jug2, target = a, b, c               # Main program
BFS(Jug1, Jug2, target)
