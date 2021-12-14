from intcode import Intcode
from itertools import permutations


def part1():
    #file = open("07/example.txt","r")
    #file = open("07/example2.txt","r")
    #file = open("07/example3.txt","r")
    #file = open("07/input.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))

    outputs = []
    ps = permutations(range(5))
    for p in ps:
        inputparams = [0]
        for phase in p:
            inputparams = inputparams + [phase]
            intcode = Intcode(inputparams)
            intcode.exec(prog)
            inputparams = intcode.output
        outputs = outputs + intcode.output
    print(max(outputs))

if __name__ == "__main__":
    part1()