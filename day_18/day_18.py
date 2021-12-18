from math import ceil,floor

def l2s(l):
    o = ''
    for x in l:
        o +=x
    return o

def new_num(n):
    if n < 10:
        return str(n)
    else:
        l = floor(n/2)
        r = ceil(n/2)
        return ['[' ,str(l) ,',' , str(r) , ']']

def process_once(num):
    i = 1
    depth = 0
    while i < len(num):
        print(i,num[i])
        if depth == 4:
            j = i+2
            print(num[i],num[i+1],num[i+2],num[i+3])
            r = int(num[j])
            j+=1
            while j < len(num) and not num[j].isnumeric():
                j+=1
            # print('jr',r,j,num[j])
            if j < len(num):
                newr = new_num(int(num[j]) + r)
                if len(newr) == 1:
                    num[j] = newr
                else:
                    num = num[:j] + newr + num[j+1:]
            # print(l2s(num))
            j = i
            l = int(num[j])
            j-=1
            while j >= 0 and not num[j].isnumeric():
                j-=1
            #print('jl',l,j,num[j])
            newl = ''
            if j > 0:
                newl = new_num(int(num[j]) + l)
                if len(newl) == 1:
                    num[j] = newl
                else:
                    num = num[:j] + newl + num[j+1:]
                    i += 4
            # print(l2s(num))
            ls = num[:i-1] 
            rs = num[i+4:]
            num = ls + ['0'] + rs
            # print(l2s(ls),":",l2s(rs))
            return True, num
        elif num[i] == '[':
            depth += 1
        elif num[i] == ']':
            depth -= 1
        else:
            pass
        i+=1
    return False,num

def add(num1,num2):
    return '[' + num1 + ',' + num2 + ']'

def process_fully(num):
    work = True
    num = list(num)
    while work:
        #print(l2s(num),'m')
        work,num = process_once(num)
    return l2s(num)

def repeated_add(filename):
    file = open(filename,"r")

    num = file.readline()[:-1]
    num = process_fully(num)
    for l in file:
        l = l[:-1]
        l = process_fully(l)
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
        num = t[0]
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
        num = s[0]
        s = s[1].split('=')
        num2 = s[0]
        numr = s[1]
        num = add(num,num2)
        num = process_fully(num)
        if l2s(num) != numr:
            print('\nresult:', l2s(num), '\nactual:',numr)
        else:
            print('\tPass')



#tester()
tester2()
