name1 = input("Player 1 what's your name?")
name2 = input("Player 2 what's your name?")
table1 = [7, 8, 9, 4, 5, 6, 1, 2, 3]
table2 = [21,22,23,24,25,16,17,18,19,20,]
tableselected = input("Choose a table bro, 3x3 or 5x5?")

def board():
    for i in range(len(table)):
        print("|", table[i], "|", end="")
        if i % 3 == 2:
            print()


def p1shot():
    k = int(input("number:"))
    num = table.index(k)
    if k in range(len(table)):
        table.insert(num, "X")
        table.remove(k)
    board()


def p2shot():
    m = int(input("number:"))
    num1 = table.index(m)
    if m in range(len(table)):
        table.insert(num1, "O")
        table.remove(m)
    board()


def win():
    if table[0] == x:
    pass
    for i in range(1,8,tableselected):
        if a[i] == X and a[i+1] == X and a[i+2]:
            win

    
board()
p1shot()
p2shot()