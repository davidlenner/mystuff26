def boardsize():
    z = 0
    u = tablesize
    for x in range(1, (tablesize*tablesize)+1):
        g.append(x)
    for i in range(tablesize):
        my_list.append(g[z:u])
        z += tablesize
        u += tablesize


def board():
    t = tablesize*tablesize
    t = len(str(t))
    for y in range(0, len(my_list)):
        sor_string = " "
        for x in range(0, len(my_list[y])):
            sor_string += str('{:{z}{u}}'.format(my_list[y][x], z='>', u=t)) + " "
        print(sor_string)


def p1shot():
    k = int(input("number1:"))
    for r in range(0, len(my_list)):
        for z in range(0, len(my_list[r])):
            if k in my_list[r]:
                num = my_list[r].index(k)
                my_list[r].insert(num,"x")
                my_list[r].remove(k)
    board()


def p2shot():
    k = int(input("number2:"))
    for r in range(0, len(my_list)):
        for z in range(0, len(my_list[r])):
            if k in my_list[r]:
                num = my_list[r].index(k)
                my_list[r].insert(num,"o")
                my_list[r].remove(k)
    board()


tablesize = int(input("choose your gamearea size:"))
my_list = []
g = []
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
        