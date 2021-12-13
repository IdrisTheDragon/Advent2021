
file = open("input.txt","r")
# file = open("input25.txt","r") ## reddit https://www.reddit.com/r/adventofcode/comments/rfeuic/2021_day_13_part_25_what_if_it_would_be_more/

grid = []
folds = []
c = True
for l in file:
    if l == "\n":
        c = False
    elif c:
        s = l[:-1].split(",")
        grid.append( (int(s[0]),int(s[1])) )
    else:
        s = l[11:-1].split("=")
        folds.append((s[0],int(s[1])))
#print(grid)
#print(folds)

def fold(f,grid):
    temp = []
    for (x,y) in grid:
        if f[0] == 'y':
            p = f[1]
            if p < y:
                dif = y - p
                newY = p - dif
                temp.append((x,newY))
            else:
                temp.append((x,y))
        elif f[0] == 'x':
            p = f[1]
            if p < x:
                dif = x - p
                newX = p - dif
                temp.append((newX,y))
            else:
                temp.append((x,y))
    return temp

grid1 = fold(folds[0],grid)
unique = set(grid1)
#print(unique)
print(len(unique))

for f in folds:
    grid = fold(f,grid)

def get_x(a):
    return a[0]

def get_y(a):
    return a[1]


x = list(map(get_x,grid))
y = list(map(get_y,grid))

maxX = max(x)
maxY = max(y)

printGrid = [[" " for i in range(maxX+1)] for j in range(maxY+1)]

for c in grid:
    printGrid[c[1]][c[0]] = "#"

for row in printGrid:
    r = ""
    for m in row:
        r = r+m
    print(r)
