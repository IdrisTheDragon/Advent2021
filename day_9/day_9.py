

file = open("example.txt","r")
neighbours = [(1,0),(-1,0),(0,1),(0,-1)]

grid = []
for l in file:
    grid.append(list(map(int,l[:-1])))

#print(grid)

risklevel =0
for x in range(0,len(grid)):
    for y in range(0,len(grid[0])):
        e = grid[x][y]
        low = True
        #print("e",e)
        for (a,b) in neighbours:
            if 0 <= x+a < len(grid) and 0 <= y+b < len(grid[0]):
                #print(x+a,y+b,grid[x+a][y+b])
                if e >= grid[x+a][y+b]:
                    low = False
        if low:
            #print(e)
            risklevel = risklevel + 1 + e
print(risklevel)

def walkneighbours(x,y,grid):
    inbasin = set()
    e = grid[x][y]
    for (a,b) in neighbours:
            if 0 <= x+a < len(grid) and 0 <= y+b < len(grid[0]):
                if e < grid[x+a][y+b] and not grid[x+a][y+b] == 9:
                    inbasin.add((x+a,y+b)) 
                    inbasin = inbasin.union(walkneighbours(x+a,y+b,grid))
    return inbasin

basins = []
for x in range(0,len(grid)):
    for y in range(0,len(grid[0])):
        e = grid[x][y]
        low = True
        #print("e",e)
        for (a,b) in neighbours:
            if 0 <= x+a < len(grid) and 0 <= y+b < len(grid[0]):
                #print(x+a,y+b,grid[x+a][y+b])
                if e >= grid[x+a][y+b]:
                    low = False
        if low:
            basin = set()
            basin.add((x,y))
            basin = basin.union(walkneighbours(x,y,grid))
            #print(len(basin))
            basins.append(len(basin))

basins.sort()
#print(basins)
print(basins[-1]*basins[-2]*basins[-3])
