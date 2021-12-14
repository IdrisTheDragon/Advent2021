from intcode import Intcode

def main():
    file = open("05/input_05.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    
    inputparams = []
    inputparams.append(1)
    intcode = Intcode(inputparams)
    intcode.exec(prog)
    print("Part 1",intcode.output)

    inputparams = []
    inputparams.append(5)
    intcode = Intcode(inputparams)
    intcode.exec(prog)
    print("Part 2",intcode.output)

if __name__ == "__main__":
    main()
    