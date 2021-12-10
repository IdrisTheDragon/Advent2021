

file = open("input.txt", "r")

fish = list(map(int, file.readline().split(",")))


# naive approach using array's..
# days = 256

# for day in range(1,days+1):
#     #print(fish)
#     newfish = 0
#     for x in range(0,len(fish)):
#         f = fish[x]
#         f = f-1
#         if f == -1:
#             f=6
#             newfish=newfish+1
#         fish[x] = f
#     for x in range(0,newfish):
#         fish.append(8)
# print(len(fish))

#advanced approach using dict as exponential growth..
fishes = dict()

for f in fish:
    if f in fishes.keys():
        fishes[f] = fishes[f]+1
    else:
        fishes[f] = 1
days = 256

for day in range(1,days+1):
    tempfishes = dict()
    for k,v in fishes.items():
        n = k-1
        if n == -1:
            if 6 in tempfishes.keys():
                tempfishes[6] = tempfishes[6]+v
            else:
                tempfishes[6] = v
            tempfishes[8] = v
        else:
            if n == 6:
                if 6 in tempfishes.keys():
                    tempfishes[6] = tempfishes[6]+v
                else:
                    tempfishes[6] = v
            else:
                tempfishes[n] = v
    fishes = tempfishes

sum = 0
for f in fishes.values():
    sum = sum+f

print(sum)
