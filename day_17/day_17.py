
def process_v(vx,vy,x1,x2,y1,y2):
    px,py = 0,0
    maxHeight = 0
    while True:
        if x1 <= px <= x2 and y1 <= py <= y2:
            # inside target area
            return maxHeight
        if px > x2 or py < y1:
            # over shot target area
            return None
        px += vx
        py += vy
        maxHeight = py if py > maxHeight else maxHeight
        vx = vx + 1 if vx < 0 else (vx - 1 if vx > 0 else 0)
        vy += -1

file = open("input.txt","r")

l = file.readline()[:-1].split(" ")
x = l[2].split("=")[1].split("..")
y = l[3].split("=")[1].split("..")
x1,x2 = int(x[0]),int(x[1][:-1])
y1,y2 = int(y[0]),int(y[1])
print("x",x1,x2,"y",y1,y2)


maxHeight = 0
maxX,maxY = 0,0
every = []

for vx in range(0,x2+2):
    for vy in range(y1-2,1000):
        #vx,vy = 6,9
        h = process_v(vx,vy,x1,x2,y1,y2)
        if not h == None:
            every.append((vx,vy))
            if h > maxHeight:
                maxHeight = h
                maxX = vx
                maxY = vy

print(maxHeight,maxX,maxY)
print(len(every))

