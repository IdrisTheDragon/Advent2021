from collections import defaultdict
file = open("input.txt","r")

poly = file.readline()[:-1]
file.readline()

links = dict()

for l in file:
    s = l[:-1].split(" -> ")
    links[s[0]] = s[1]

#print(links)
def part1(poly):
    poly = poly.copy()
    for i in range(0,10):
        #print(i,poly)
        temp = ""
        for j in range(0,len(poly)-1):
            n = poly[j:j+2]
            #print(n)
            if n in links.keys():
                temp = temp + n[0] + links[n]
        temp = temp + poly[-1]
        poly = temp

    #print(len(poly))

    buckets = dict()

    for x in poly:
        if x in buckets.keys():
            buckets[x] +=1
        else:
            buckets[x] = 1


    m = max(buckets.values())
    mi = min(buckets.values())
    print(m-mi)

# part1(poly)

pairs = defaultdict(int)
individuals = defaultdict(int)

for i in range(0, len(poly)-1):
    pairs[poly[i] + poly[i+1]] += 1
    individuals[poly[i]] += 1
individuals[poly[-1]] += 1

for i in range(0,40):
    temp_pairs = defaultdict(int)

    for p in pairs.keys():
        if p in links.keys():
            individuals[links[p]] += pairs[p]
            temp_pairs[p[0] + links[p]] += pairs[p]
            temp_pairs[links[p] + p[1]] += pairs[p]

    pairs = temp_pairs




m = max(individuals.values())
mi = min(individuals.values())
print(m-mi)
