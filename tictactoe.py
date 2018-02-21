import sys

tablesize = int(input("choose a board size(3 or 5):"))


def board():
    if tablesize == 3:
        for i in range(len(table)):
            print("|", table[i], "|", end="")
            if i % 3 == 2:
                print()
    if tablesize == 5:
        for i in range(len(table)):
            print("|", "%2s" % table[i], "|", end="")
            if (i+1) % 5 == 0:
                print()


def p1shot():
    k = int(input("number:"))
    num = table.index(k)
    if num in range(len(table)):
        table.insert(num, "x")
        table.remove(k)
    board()
    for i in range(0, 8):
        if table[i] == "x" and table[i+1] == "x" and table[i+2] == "x":
            print("win")
            exit()
        elif table[i] == "x" and table[i+3] == "x" and table[i+6] == "x":
            print("win")
            exit()
        elif table[i] == "x" and table[i+4] == "x" and table[i+8] == "x":
            print("win")
            exit()
        elif table[i+2] == "x" and table[i+4] == "x" and table[i+6] == "x":
            print("win")
            exit()

def p2shot():
    m = int(input("number:"))
    num1 = table.index(m)
    if num1 in range(len(table)):
        table.insert(num1, "0")
        table.remove(m)
    board()
    for i in range(0, 8):
        if table[i] == "0" and table[i+1] == "0" and table[i+2] == "0":
            print("win")
            exit()
        elif table[i] == "0" and table[i+3] == "0" and table[i+6] == "0":
            print("win")
            exit()
        elif table[i] == "0" and table[i+4] == "0" and table[i+8] == "0":
            print("win")
            exit()
        elif table[i+2] == "0" and table[i+4] == "0" and table[i+6] == "0":
            print("win")
            exit()

        
def boardsize():
    if tablesize == 3:
        while len(table) != tablesize*tablesize:
            for i in range(7-(len(table)),10-(len(table))):
                table.append(i)
    if tablesize == 5:
        while len(table) != tablesize*tablesize:
            for i in range(21-(len(table)), 26-(len(table))):
                table.append(i)


table = []
boardsize()
board()
while True:
    try:
        p1shot()
    except(IndexError, ValueError):
        pass
    try:
        p2shot()
    except(IndexError, ValueError):
        pass

