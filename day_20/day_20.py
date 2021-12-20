
neighbours = [(-1,-1),(0,-1),(1,-1),
                (-1,0),(0,0),(1,0),
                (-1,1),(0,1),(1,1)]
#neighbours.reverse()

file = open("input.txt","r") 
# note: inputs with static background won't work. (example.txt) remove commented sections.

grid = set()

enhance = file.readline()[:-1]
file.readline()

maxX = 0
maxY = 0
minX = 0-55
minY = 0-55
for y,l in enumerate(file):
    l = l[:-1]
    if y > maxY:
        maxY = y
    for x,v in enumerate(l):
        if x > maxX:
            maxX = x
        if v == '#':
            grid.add((x,y))

maxX +=55
maxY +=55
#print(grid)

def render_grid(grid):
    mx = max(grid,key=lambda item:item[0])
    Mx = min(grid,key=lambda item:item[0])
    my = max(grid,key=lambda item:item[1])
    My = min(grid,key=lambda item:item[1])
    #print(mx[0],Mx[0],my[1],My[1])
    for y in range(My[1]-1,my[1]+2):
        l = ""
        for x in range(Mx[0]-1,mx[0]+2):
            if (x,y) in grid:
                l += '#'
            else:
                l+= '.'
        print(l)




def process_grid(grid,odd=False):
    newgrid = set()
    for x in range(minX,maxX):
        for y in range(minY,maxY):
            #print(x,y)
            num = ''
            for (a,b) in neighbours:
                #if x == 2 and y == 2:
                #    print((x+a,y+b),(x+a,y+b) in grid)
                # remove start - for static background
                if odd:
                    if (x+a,y+b) in grid:
                        num += '0'
                    else:
                        num += '1'
                else:
                # remove end
                    if (x+a,y+b) in grid:
                        num += '1'
                    else:
                        num += '0'           #if x ==2 and y == 2:
            #    print(num)
            
            num = int(num,2)

            newV = enhance[num]
            #remove start - for static background
            if not odd:
                if newV == '.':
                    newgrid.add((x,y))
            else:
            # remove end
                if newV == '#':
                    newgrid.add((x,y))
    return newgrid

#render_grid(grid)
#print()
for _ in range(0,25): # (0,1) for part 1 # (0,25) for part 2, (each iteration does process twice to handle the alternating background)
    grid = process_grid(grid)
    #render_grid(grid)
    print(len(grid))
    grid = process_grid(grid,True)
    # print(grid)
    #render_grid(grid)
    print(len(grid))

