from time import sleep

def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def int_input():
    return int(input("Enter a number:"))
def output_int(a):
    print(a)
def jump_if_true(a,b):
    if a != 0:
        return b
    return None
def jump_if_false(a,b):
    if a == 0:
        return b
    return None
def less_than(a,b):
    if a < b:
        return 1
    return 0
def equals(a,b):
    if a == b:
        return 1
    return 0

ops = {
    1:(2,1,add),
    2:(2,1,multiply),
    3:(0,1,int_input),
    4:(1,0,output_int),
    5:(1,1,jump_if_true),
    6:(1,1,jump_if_false),
    7:(2,1,less_than),
    8:(2,1,equals),
    99:None}

def execintcode(prog):
    mem = prog.copy()

    pointer = 0

    while True:
        #print(pointer,mem)
        instruction = mem[pointer]
        instruction = str(instruction)
        op = int(instruction[-2:])
        p1,p2,p3 = 0,0,0
        if len(instruction) >= 3:
            p1 = int(instruction[-3])
        if len(instruction) >= 4:
            p2 = int(instruction[-4])
        if len(instruction) >= 5:
            p3 = int(instruction[-5])
        # print(instruction)
        # print(mem)
        # sleep(1)
        opc = ops[op]
        if opc == None:
            break
        if opc[0] == 2 and opc[1] == 1:
            a = mem[pointer+1]
            b = mem[pointer+2]
            c = mem[pointer+3]
            a = mem[a] if p1 == 0 else a
            b = mem[b] if p2 == 0 else b
            mem[c] = opc[2](a,b)
            pointer = pointer+4
        elif opc[0] == 1 and opc[1] == 0:
            a = mem[pointer+1]
            a = mem[a] if p1 == 0 else a
            opc[2](a)
            pointer = pointer + 2
        elif opc[0] == 0 and opc[1] == 1:
            a = mem[pointer+1]
            mem[a] = opc[2]()
            pointer = pointer + 2
        elif op in [5,6]:
            a = mem[pointer+1]
            b = mem[pointer+2]
            a = mem[a] if p1 == 0 else a
            b = mem[b] if p2 == 0 else b
            pointer = opc[2](a,b) if opc[2](a,b) != None else pointer + 3

        
    return mem

def main():
    file = open("input.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    mem = execintcode(prog)

if __name__ == "__main__":
    main()
    