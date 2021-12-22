

file = open("input.txt", "r")

cubes = set()

for l in file:
    s = l[:-1].split(" ")
    state = s[0]
    s = s[1].split(",")
    xs = s[0].split("=")
    xs = xs[1].split("..")

    ys = s[1].split("=")
    ys = ys[1].split("..")

    zs = s[2].split("=")
    zs = zs[1].split("..")

    #print(zs)
    # for x in range(int(xs[0]),int(xs[1])+1):
    #     for y in range(int(ys[0]),int(ys[1])+1):
    #         for z in range(int(zs[0]),int(zs[1])+1):
    for x in range(max(int(xs[0]),-50),min(int(xs[1]),50)+1):
        for y in range(max(int(ys[0]),-50),min(int(ys[1]),50)+1):
            for z in range(max(int(zs[0]),-50),min(int(zs[1]),50)+1):
                if state == 'on':
                    cubes.add((x,y,z))
                else:
                    try:
                        cubes.remove((x,y,z))
                    except:
                        pass

#print(cubes)
print(len(cubes))

