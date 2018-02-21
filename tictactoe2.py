tablesize = int(input("gfdg:"))


def board1():
    while len(board) != tablesize:
        for i in range(tablesize):
            board.append([])
        print(board)
    
        
board = []
g = []
board1()

def board2():
    for i in board:
        for i in range(tablesize):
            board.append(i)
        print(board)
board2()



