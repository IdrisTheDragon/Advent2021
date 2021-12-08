#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

file = open("input.txt")

simple = {2:1,4:4,3:7,7:8}

part1 = 0

def part1s(o):
    global part1
    for x in o:
        if len(x) in simple.keys():
            part1 = part1 + 1

part2 = 0
for line in file:
    split = line[:-1].split("|")
    iin = split[0][:-1].split(" ")
    oout = split[1][1:].split(" ")
    part1s(oout)

    chars = {0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set(),9:set()}
    for x in iin:
        if len(x) in simple.keys():
            chars[simple[len(x)]] = set(x)

    n = ''
    for o in map(set, oout):
        a = o&chars[8]
        b = o&chars[4]
        c = o&chars[1]
        if len(a) == 6 and len(b) == 3 and len(c) == 2:
            n += '0'
            chars[0] = o
        elif len(a) == 2 and len(b) == 2 and len(c) == 2:
            n += '1'
        elif len(a) == 5 and len(b) == 2 and len(c) == 1:
            n += '2'
            chars[2] = o
        elif len(a) == 5 and len(b) == 3 and len(c) == 2:
            n += '3'
            chars[3] = o
        elif len(a) == 4 and len(b) == 4 and len(c) == 2:
            n += '4'
        elif len(a) == 5 and len(b) == 3 and len(c) == 1:
            n += '5'
            chars[5] = o
        elif len(a) == 6 and len(b) == 3 and len(c) == 1:
            n += '6'
            chars[6] = o
        elif len(a) == 3 and len(b) == 2 and len(c) == 2:
            n += '7'
        elif len(a) == 7 and len(b) == 4 and len(c) == 2:
            n += '8'
        elif len(a) == 6 and len(b) == 4 and len(c) == 2:
            n += '9'
            chars[9] = o
        else:
            print("broke")
    # print(int(n))
    # print(chars)
    part2 += int(n)

    
    
print("part 1:",part1)
print("part 2:",part2)