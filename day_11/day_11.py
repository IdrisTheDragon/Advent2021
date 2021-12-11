file = open("input.txt","r")

grid = []
neighbours = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]


for l in file:
    grid.append(list(map(int,l[:-1])))

def gridprint(g):
    for l in g:
        print(l)
    print()

steps = 1000
count = 0
for i in range(0,steps):
    for x in range(0,len(grid)):
        for y in range(0,len(grid[0])):
            grid[x][y] += 1
    updated = True
    while updated:
        updated = False
        for x in range(0,len(grid)):
            for y in range(0,len(grid[0])):
                if grid[x][y] > 9:
                    grid[x][y] = 0
                    for (a,b) in neighbours:
                         if 0 <= x+a < len(grid) and 0 <= y+b < len(grid[0]):
                            if not grid[x+a][y+b] == 0:
                                grid[x+a][y+b] +=1
                                updated = True
    stepc=0
    for x in range(0,len(grid)):
        for y in range(0,len(grid[0])):
            if grid[x][y] == 0:
                count += 1
                stepc += 1
    if stepc == 100:
        #part2
        print(i+1)
        break
    if i == 99:
        #part1
        print(count)
    #gridprint(grid)
#print(count)

