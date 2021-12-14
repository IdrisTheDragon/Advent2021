from intcode import Intcode

def main():
    file = open("02/example_02.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    intcode = Intcode()
    intcode.exec(prog)

    file = open("02/input_02.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    prog[1] = 12
    prog[2] = 2
    intcode = Intcode()
    intcode.exec(prog)
    mem = intcode.mem
    print(mem[0]) # part 1

    for noun in range(0,99):
        for verb in range(0,99):
            prog[1] = noun
            prog[2] = verb
            intcode.exec(prog)
            mem = intcode.mem
            if mem[0] == 19690720:
                print(100*noun+verb) # part 2
                return 0

if __name__ == "__main__":
    main()
    