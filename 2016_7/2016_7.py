
file = open("input.txt","r")

valid = 0

for l in file:
    l = l[:-1]
    cur = []
    hypernet = []
    normal = []
    for c in l:
        if c == '[':
            normal.append(cur)
            cur = []
        elif c == ']':
            hypernet.append(cur)
            cur = []
        else:
            cur.append(c)
    normal.append(cur)
    
    isInvalid = False
    for l in hypernet:
        for i in range(0,len(l)-3):
            if l[i +1] == l[i + 2] and l[i] == l[i + 3] and l[i] != l[i+1]:
                isInvalid = True
                break
        if isInvalid:
            break
    if isInvalid:
        continue
    
    isValid = False
    for l in normal:
        for i in range(0,len(l)-3):
            if l[i +1] == l[i + 2] and l[i] == l[i + 3] and l[i] != l[i+1]:
                isValid = True
                break
        if isValid:
            break
    if isValid:
        valid = valid + 1

print(valid)

