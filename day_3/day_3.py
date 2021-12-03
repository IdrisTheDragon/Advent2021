

file = open("example.txt", "r")

count1 = []
count0 = []
x = file.readline()
x = x[:-1]
for v in x:
    if v == '0':
        count0.append(1)
        count1.append(0)
    elif v == '1':
        count0.append(0)
        count1.append(1)
    else:
        print("invalid",v)
for x in file:
    x = x[:-1]
    for y,v in enumerate(x):
        if v == '0':
            count0[y] = count0[y] +1
        elif v == '1':
            count1[y] = count1[y] +1
        else:
            print("invalid",v)
epsilon = []
gamma = []
for x in range(0,len(count0)):
    if count1[x] > count0[x]:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print(count0,count1)
print(gamma,epsilon)

gamma = int("".join(str(i) for i in gamma),2)
epsilon = int("".join(str(i) for i in epsilon),2)
print(gamma,epsilon)
print(gamma*epsilon)


file = open("input.txt", "r")
values = []
values2 = []
for x in file:
    values.append(x[:-1])
    values2.append(x[:-1])

index = 0
while len(values) > 1:
    temp = []
    c0 = 0
    c1 = 0
    for x in values:
        if x[index] == '0':
            c0 = c0 + 1
        else:
            c1 = c1 + 1
    #print(values)
    #print(c0, c1)
    if c0 > c1:
        for x in values:
            if x[index] == '0':
                temp.append(x)
    else:
        for x in values:
            if x[index] == '1':
                temp.append(x)
    values = temp
    index = index + 1
    if index == len(values[0]):
        index = 0
    
print(values[0])

index = 0
while len(values2) > 1:
    temp = []
    c0 = 0
    c1 = 0
    for x in values2:
        if x[index] == '0':
            c0 = c0 + 1
        else:
            c1 = c1 + 1
    #print(values2)
    #print(c0, c1)
    if c0 <= c1:
        for x in values2:
            if x[index] == '0':
                temp.append(x)
    else:
        for x in values2:
            if x[index] == '1':
                temp.append(x)
    values2 = temp
    index = index + 1
    if index == len(values2[0]):
        index = 0
    
print(values2[0])

gamma = int("".join(str(i) for i in values[0]),2)
epsilon = int("".join(str(i) for i in values2[0]),2)
print(gamma,epsilon)
print(gamma*epsilon)