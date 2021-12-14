
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

class Intcode:

    def int_input(self):
        return self.input.pop()

    def output_int(self,a):
        self.output.append(a)
    
    def __init__(self, input=None):

        self.ops = {
            1:(2,1,add),
            2:(2,1,multiply),
            3:(0,1,int_input),
            4:(1,0,output_int),
            5:(1,1,jump_if_true),
            6:(1,1,jump_if_false),
            7:(2,1,less_than),
            8:(2,1,equals),
            99:None}

        self.input = input
        if self.input != None:
            self.ops[3] = (0,1,self.int_input)
            self.ops[4] = (1,0,self.output_int)
            self.output = []

    def exec(self,prog):
        self.mem = prog.copy()
        self.pointer = 0
        

        while True:
            #print(self.pointer,self.mem)
            instruction = self.mem[self.pointer]
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
            # print(self.mem)
            # sleep(1)
            opc = self.ops[op]
            if opc == None:
                break
            if opc[0] == 2 and opc[1] == 1:
                a = self.mem[self.pointer+1]
                b = self.mem[self.pointer+2]
                c = self.mem[self.pointer+3]
                a = self.mem[a] if p1 == 0 else a
                b = self.mem[b] if p2 == 0 else b
                self.mem[c] = opc[2](a,b)
                self.pointer = self.pointer+4
            elif opc[0] == 1 and opc[1] == 0:
                a = self.mem[self.pointer+1]
                a = self.mem[a] if p1 == 0 else a
                opc[2](a)
                self.pointer = self.pointer + 2
            elif opc[0] == 0 and opc[1] == 1:
                a = self.mem[self.pointer+1]
                self.mem[a] = opc[2]()
                self.pointer = self.pointer + 2
            elif op in [5,6]:
                a = self.mem[self.pointer+1]
                b = self.mem[self.pointer+2]
                a = self.mem[a] if p1 == 0 else a
                b = self.mem[b] if p2 == 0 else b
                self.pointer = opc[2](a,b) if opc[2](a,b) != None else self.pointer + 3
