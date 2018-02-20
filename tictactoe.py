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
    for i in range(0, 8, 3):
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


table = [] 
while len(table) != 9:
    for i in range(7-(len(table)),10-(len(table))):
        table.append(i)
print(table)


table = []       
board()
while True:
    try:
        p1shot()
    except(IndexError,):
        pass
    try:
        p2shot()
    except(IndexError,):
        pass
