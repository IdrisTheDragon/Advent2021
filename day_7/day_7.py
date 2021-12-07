

file = open("input.txt","r")

crabs = list(map(int,file.readline().split(",")))



def costto(num,crabs):
    sum = 0
    for c in crabs:
        s = c-num
        sum = sum + abs(s)
    return sum

def coststeps(steps):
    # sum = 0
    # for i in range(1,steps+1):
    #     sum = sum+i
    # return sum
    return int(((1+steps)/2)*steps)

def costto2(num,crabs):
    sum = 0
    for c in crabs:
        s = c-num
        sum = sum + coststeps(abs(s))
    return sum

m = min(crabs)
M = max(crabs)

min = 20000000000
for i in range(m,M):
    s = costto(i,crabs)
    if min > s:
        min = s
print(min)

min = 20000000000
for i in range(m,M):
    s = costto2(i,crabs)
    if min > s:
        min = s
print(min)