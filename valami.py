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
        for x in range(0, (tablesize+1)):
            try:
                ertek = my_list[y][x]
                bal_szomszed = my_list[y][x - 1]
                jobb_szomszed = my_list[y][x + 1]
                felso_szomszed = my_list[y - 1][x]
                also_szomszed = my_list[y + 1][x]
                bal_felso_szomszed = my_list[y - 1][x - 1]
                jobb_also_szomszed = my_list[y + 1][x + 1]
                jobb_felso_szomszed = my_list[y - 1][x + 1]
                bal_also_szomszed = my_list[y + 1][x - 1]
                if (ertek == bal_szomszed and ertek == jobb_szomszed):
                    print(ertek + " win")
                    exit()
                if (ertek == also_szomszed and ertek == felso_szomszed):
                    print(ertek + " win")
                    exit()
                if (ertek == bal_felso_szomszed and ertek == jobb_also_szomszed):
                    print(ertek + " win")
                    exit()
                if (ertek == bal_also_szomszed and ertek == jobb_felso_szomszed):
                    print(ertek + " win")
                    exit()
            except(IndexError):
                continue


def p1shot():
    k = int(input("%s write a number:" % name1))
    while k in shots or k > tablesize*tablesize:
        k = int(input("%s write a number:" % name1))
    shots.append(k)
    for r in range(0, len(my_list)):
        for z in range(0, len(my_list[r])):
            if k in my_list[r]:
                num = my_list[r].index(k)
                my_list[r].insert(num, "x")
                my_list[r].remove(k)
    board()


def p2shot():
    k = int(input("%s write a number:" % name2))
    while k in shots or k > tablesize*tablesize:
        k = int(input("%s write a number:" % name2))
    shots.append(k)
    for r in range(0, len(my_list)):
        for z in range(0, len(my_list[r])):
            if k in my_list[r]:
                num = my_list[r].index(k)
                my_list[r].insert(num, "o")
                my_list[r].remove(k)
    board()


def main():
    stage = 0
    while stage < tablesize*tablesize:
        p1shot()
        stage += 1
        if stage == tablesize*tablesize:
            print("TIE!!")
            break
        investigate()
        p2shot()
        stage += 1
        investigate()


name1 = input("Player 1 what's your name?")
name2 = input("Player 2 what's your name?")
tablesize = int(input("Choose your gamearea size:"))
while tablesize > 10 or tablesize < 3:
    tablesize = int(input("Choose your gamearea size:"))
my_list = []
g = []
shots = []
boardsize()
board()

main()
