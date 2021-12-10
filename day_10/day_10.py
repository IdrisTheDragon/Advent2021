
from stack import Stack

file = open("input.txt", "r")

o = {')':'(',']':'[','}':'{','>':'<'}
points = {')':3,']':57,'}':1197,'>':25137}
points2 = {'(':1,'[':2,'{':3,'<':4}
def validate(l):
    op = Stack()
    for x in l:
        if x in o.values():
            op.push(x)
        elif x in o.keys():
            if op.peek() == o[x]:
                op.pop()
            else:
                #print("invalid",l, "expected", op.peek(), "found", x)
                return x
    return op

sum2 = []
sum = 0
for l in file:
    x = validate(l[:-1])
    if isinstance(x,str):
        # part 1
        sum = sum + points[x]
    elif isinstance(x,Stack):
        s = 0
        while not x.isEmpty():
            t = x.pop()
            score = points2[t]
            s = s*5+score
        sum2.append(s)
    else:
        print("invalid return type")

print(sum)
#print(sum2)
sum2.sort()
print(sum2[int(len(sum2)/2)])