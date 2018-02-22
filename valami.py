def boardsize():
    z = 0
    u = tablesize
    for x in range(1, (tablesize*tablesize)+1):
        g.append(x)
    for x in range(tablesize):
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


def investigate():
    for y in range(0, tablesize):
        for x in range(0, len(my_list[y])):
            try:
                ertek = my_list[y][x] #a fenti listán belüli második(y = 1) my_list második(x = 1) elemének az értéke(5)
                bal_szomszed = my_list[y][x - 1] #az x és y koordináta bal oldali szomszédjának az értéke(4)
                jobb_szomszed = my_list[y][x + 1] #az x és y koordináta jobb oldali szomszédjának az értéke(6)
                felso_szomszed = my_list[y - 1][x] #az x és y koordináta felső szomszédjának az értéke(2)
                also_szomszed = my_list[y + 1][x] #az x és y koordináta alsó szomszédjának az értéke(8)
                bal_felso_szomszed = my_list[y - 1][x - 1] #az x és y koordináta bal felső szomszédjának az értéke(1)
                if ertek == "x" and bal_szomszed == "x" and jobb_szomszed == "x":
                    print("WIN")
                    exit()
                if ertek == "x" and felso_szomszed == "x" and also_szomszed == "x":
                    print("WIN")
                    exit()
                
                except(IndexError):
                    pass


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
        investigate()
    except(IndexError, ValueError):
        pass
    try:
        p2shot()
        investigate()
    except(IndexError, ValueError):
        pass
        