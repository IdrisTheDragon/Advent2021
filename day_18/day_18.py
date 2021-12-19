from math import ceil,floor

def l2s(l):
    o = ''
    for x in l:
        o += str(x)
    return o


def new_num(n):
    l = floor(n/2)
    r = ceil(n/2)
    return ['[' ,l,',' , r, ']']


def s2l(l):
    o = []
    for x in l:
        if x.isnumeric():
            x = int(x)
        o.append(x)
    return o

def add(num1,num2):
    return ['['] + num1 + [','] + num2 + [']']

def explode_node(num,i):
    #print(l2s(num))
    #print('should always be "[":',num[i-1])
    j = i+2
    #print(num[i],num[i+1],num[i+2],num[i+3])
    #print(num[i-1:i+4])
    r = num[j]
    j+=1
    while j < len(num) and not isinstance(num[j],int):
        j+=1
    # print('jr',r,j,num[j])
    if j < len(num):
        #print(num[j],r)
        newr = num[j] + r
        num[j] = newr
    # print(l2s(num))
    j = i
    l = num[j]
    j-=1
    while j >= 0 and not isinstance(num[j],int):
        j-=1
    #print('jl',l,j,num[j])
    newl = ''
    if j > 0:
        #print(num[j],l)
        newl = num[j] + l
        num[j] = newl
    # print(l2s(num))
    ls = num[:i-1] 
    rs = num[i+4:]
    num = ls + [0] + rs
    # print(l2s(ls),":",l2s(rs))
    return True, num

def explode_once(num):
    i = 1
    depth = 0
    while i < len(num):
        #print(i,num[i])
        if num[i] == '[':
            depth += 1
        elif num[i] == ']':
            
            if depth >= 4: # first top level node
                return explode_node(num,i-3)
            depth -= 1
        else:
            pass
        i+=1
    return False,num


def split(num):
    i = 0
    while i < len(num)-1:
        i+=1
        if isinstance(num[i],int):
            if num[i] > 9:
                new = new_num(num[i])
                num = num[:i] + new + num[i+1:]
    return num


def process_fully(num):
    work = True
    while work:
        #print(l2s(num),'m')
        work,num = explode_once(num)
        # print(l2s(num),"post explode")
        if work:
            num = split(num)
            # print(l2s(num), "post split")
    return num


def repeated_add(filename):
    file = open(filename,"r")

    num = file.readline()[:-1]
    num = s2l(num)
    for l in file:
        l = l[:-1]
        l = s2l(l)
        # print(l,num)
        num = add(num,l)
        num = process_fully(num)
    return num

tests = [
    ['[[[[[9,8],1],2],3],4]','[[[[0,9],2],3],4]'],
    ['[7,[6,[5,[4,[3,2]]]]]','[7,[6,[5,[7,0]]]]'],
    ['[[6,[5,[4,[3,2]]]],1]','[[6,[5,[7,0]]],3]'],

    #['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'],
    #['[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[7,0]]]]'],
    # Two above combine to this one
    ['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[7,0]]]]'],


    ['[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]','[[[[0,7],4],[[7,8],[6,0]]],[8,1]]']
]

tests_add = [
    ["example2.txt",'[[[[3,0],[5,3]],[4,4]],[5,5]]'],
    ["example3.txt",'[[[[5,0],[7,4]],[5,5]],[6,6]]'],
    ["example.txt",'[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'],
    ["example4.txt",'[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]']
]

def tester():
    for t in tests:
        print('Test:',t[0])
        num = s2l(t[0])
        numr = t[1]
        num = process_fully(num)
        if l2s(num) != numr:
            print('start:',t[0], '\nresult:', l2s(num), '\nactual:',numr)
        else:
            print('\tPass')
    for t in tests_add:
        print('Test:',t[0])
        filename = t[0]
        numr = t[1]
        num = repeated_add(filename)
        if l2s(num) != numr:
            print('file:',filename, '\nresult:', l2s(num), '\nactual:',numr)
        else:
            print('\tPass')


def tester2():
    file = open("long_example.txt","r")
    i = 0
    for l in file:
        i+=1
        print("Test",i)
        l = l[:-1]
        s = l.split('+')
        num = s2l(s[0])
        s = s[1].split('=')
        num2 = s2l(s[0])
        numr = s[1]
        num = add(num,num2)
        num = process_fully(num)
        if l2s(num) != numr:
            print('result:', l2s(num), '\nactual:',numr)
        else:
            print('\tPass')


def main():
    tester()
    #tester2()

if __name__ == "__main__":
    main()
