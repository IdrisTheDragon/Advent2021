from intcode import execintcode

def main():
    file = open("02/example_02.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    mem = execintcode(prog)

    file = open("02/input_02.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    prog[1] = 12
    prog[2] = 2
    mem = execintcode(prog)
    print(mem[0]) # part 1

    for noun in range(0,99):
        for verb in range(0,99):
            prog[1] = noun
            prog[2] = verb
            mem = execintcode(prog)
            if mem[0] == 19690720:
                print(100*noun+verb) # part 2
                return 0

if __name__ == "__main__":
    main()
    