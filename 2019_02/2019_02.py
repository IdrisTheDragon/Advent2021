
def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
ops = {1:(3,add),2:(3,multiply),99:None}

def execintcode(prog):
    mem = prog.copy()

    pointer = 0

    while True:
        #print(pointer,mem)
        op = mem[pointer]
        opc = ops[op]
        if opc == None:
            break
        if opc[0] == 3:
            a = mem[pointer+1]
            b = mem[pointer+2]
            c = mem[pointer+3]
            mem[c] = opc[1](mem[a],mem[b])
            pointer = pointer+4
    return mem

def main():
    file = open("example.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    mem = execintcode(prog)

    file = open("input.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    prog[1] = 12
    prog[2] = 2
    mem = execintcode(prog)
    print(mem[0])

    for noun in range(0,99):
        for verb in range(0,99):
            prog[1] = noun
            prog[2] = verb
            mem = execintcode(prog)
            if mem[0] == 19690720:
                print(100*noun+verb)
                return 0

if __name__ == "__main__":
    main()
    