from intcode import execintcode

def main():
    file = open("05/input_05.txt","r")

    prog = file.readline()[:-1].split(",")
    prog = list(map(int,prog))
    mem = execintcode(prog)

if __name__ == "__main__":
    main()
    