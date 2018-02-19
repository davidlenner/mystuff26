import sys
def board():
    for i in range(len(table)):
        print("|", table[i], "|", end="")
        if i % 3 == 2:
            print()


def p1shot():
    k = int(input("number:"))
    num = table.index(k)
    if num in range(len(table)):
        table.insert(num, "x")
        table.remove(k)
    board()
    for i in range(len(table)):
        if table[i] == "x" and table[i+1] == "x" and table[i+2] == "x":
            print("win")
            exit()


def p2shot():
    m = int(input("number:"))
    num1 = table.index(m)
    if num1 in range(len(table)):
        table.insert(num1, "O")
        table.remove(m)
    board()


table = [7, 8, 9, 4, 5, 6, 1, 2, 3]       
board()
while True:
    try:
        p1shot()
    except(IndexError):
        pass
    try:
        p2shot()
    except(IndexError):
        pass
