
file = open("input.txt","r")

grid = []

for l in file:
    grid.append(list(map(int,l[:-1])))

#print(grid)

dir = [(1,0),(0,1),(-1,0),(0,-1)]

def path_node(grid,node):
    (x,y) = node
    if x == len(grid[0])-1 and y == len(grid)-1:
        return grid[y][x]
    minCost = 500000
    for (a,b) in dir:
        if 0 <= x+a < len(grid[0]) and 0 <= y+b < len(grid):
            cost = path_node(grid,(x+a,y+b))
            if cost < minCost:
                minCost = cost
    return minCost + grid[y][x]

# cost = path_node(grid,(0,0))
# cost = cost - grid[0][0]
# print(cost)

def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)

from priority_queue import PriorityQueue

def star_search(grid,start,end):
    frontier = PriorityQueue()
    frontier.put(start,0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():

        (x,y) = frontier.get()

        if (x,y) == end:
            break
        
        for (a,b) in dir:
            if 0 <= x+a < len(grid[0]) and 0 <= y+b < len(grid):
                (x1,y1) = (x+a,y+b)
                new_cost = cost_so_far[(x,y)] + grid[y1][x1]
                if (x1,y1) not in cost_so_far or new_cost < cost_so_far[(x1,y1)]:
                    cost_so_far[(x1,y1)] = new_cost
                    priority = new_cost + heuristic((x1,y1),end)
                    frontier.put((x1,y1), priority)
                    came_from[(x1,y1)] = (x,y)
    return came_from, cost_so_far

end  = (len(grid[0])-1,len(grid)-1)
came_from, cost_so_far = star_search(grid,(0,0),end)
#print(cost_so_far)
cost = cost_so_far[end]
print(cost)  

def increment(x):
    x = x + 1
    if x == 10:
        return 1
    return x

m2 = [[increment(v) for v in r] for r in grid]
m3 = [[increment(v) for v in r] for r in m2]
m4 = [[increment(v) for v in r] for r in m3]
m5 = [[increment(v) for v in r] for r in m4]
 
m1_5 = grid + m2 +m3 + m4 + m5
grid = []
for row in m1_5:
    m2 = [increment(v) for v in row]
    m3 = [increment(v) for v in m2]
    m4 = [increment(v) for v in m3]
    m5 = [increment(v) for v in m4]
    grid.append(row + m2 + m3 + m4 + m5)

# for r in grid:
#     o = ""
#     for x in r:
#         o = o + str(x)
#     print(o)


end  = (len(grid[0])-1,len(grid)-1)
came_from, cost_so_far = star_search(grid,(0,0),end)
#print(cost_so_far)
cost = cost_so_far[end]
print(cost)  

