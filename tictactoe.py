

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




table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    
 
