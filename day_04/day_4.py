
def parse():
    file = open("input.txt", "r")

    seq = file.readline()[:-1].split(",")
    boards = []
    curBoard = None
    for x in file:
        if x == "\n":
            curBoard = []
            boards.append(curBoard)
        else:
            nums = x[:-1].split(" ")
            #print(nums)
            row = []
            curBoard.append(row)
            for y in nums:
                if y == "":
                    pass
                else:
                    row.append([y,0])
    return boards,seq

def find_winner(boards):
    for board in boards:
        for row in board:
            sum = 0
            for i in row:
                sum = sum + i[1]
            if sum == len(row):
                return board
        for x in range(0,len(board[0])-1):
            sum = 0
            for y in board:
                sum = sum + y[x][1]
            if sum == len(board[0]):
                return board
    return None

boards,seq = parse()

winner = None
lastseq = None
for x in seq:
    for board in boards:
        for row in board:
            for i in row:
                if x == i[0]:
                    i[1] = 1
    winner = find_winner(boards)
    if winner != None:
        lastseq = x
        break
sum = 0
for row in winner:
    for i in row:
        if i[1] == 0:
            sum =sum + int(i[0])
print(sum,lastseq)
print(sum*int(lastseq))



# part 2
boards,seq = parse()

lastwinner = None
lastseq = None
for x in seq:
    for board in boards:
        for row in board:
            for i in row:
                if x == i[0]:
                    i[1] = 1
    winner = 1
    while(winner != None):
        winner = None
        winner = find_winner(boards)
        if winner != None:
            boards.remove(winner)
            lastwinner = winner
            lastseq = x
sum = 0
for row in lastwinner:
    for i in row:
        if i[1] == 0:
            sum =sum + int(i[0])
print(sum,lastseq)
print(sum*int(lastseq))
    

 
