file = open("input.txt", "r")

coords=dict()
coords2=dict()

def part1(c):
    if c in coords.keys():
        coords[c] = coords[c] + 1
    else:
        coords[c] = 1

def part2(c):
    if c in coords2.keys():
        coords2[c] = coords2[c] + 1
    else:
        coords2[c] = 1

for l in file:
    s = l[:-1].split(" ")
    #print(s)
    xy1 = s[0].split(",")
    xy2 = s[2].split(",")
    if xy1[0] == xy2[0]:
        x = int(xy1[0])
        (y1,y2) = (int(xy2[1]),int(xy1[1])) if  int(xy1[1]) > int(xy2[1]) else (int(xy1[1]),int(xy2[1]))
        for y in range(y1,y2+1):
            part1((x,y))
            part2((x,y))
    elif xy1[1] == xy2[1]:
        y = int(xy1[1])
        (x1,x2) = (int(xy2[0]),int(xy1[0])) if  int(xy1[0]) > int(xy2[0]) else (int(xy1[0]),int(xy2[0]))
        for x in range(x1,x2+1):
            part1((x,y))
            part2((x,y))
    else:
        print(s)
        (x1,x2) = (int(xy1[0]),int(xy2[0]))
        (y1,y2) = (int(xy1[1]),int(xy2[1]))
        (s1,s2) = (int(xy2[0]),int(xy1[0])) if  int(xy1[0]) > int(xy2[0]) else (int(xy1[0]),int(xy2[0]))
        for i in range(0,s2-s1+1):
            x = x1+i if x1<x2 else x1-i
            y = y1+i if y1<y2 else y1-i
            print((x,y))
            part2((x,y))
#print(coords2)

sum = 0
for x in coords.values():
    if x > 1:
        sum = sum + 1

print(sum)

sum2 = 0
for x in coords2.values():
    if x > 1:
        sum2 = sum2 + 1

print(sum2)