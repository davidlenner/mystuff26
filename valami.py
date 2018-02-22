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
    for x in range(0,tablesize):
        for y in range(0, len(my_list[x])):
            try:    
                ertek = my_list[y][x] #a fenti listán belüli második(y = 1) my_list második(x = 1) elemének az értéke(5)
                print("Jelenlegi pozíció értéke:", ertek)

                bal_szomszed = my_list[y][x - 1] #az x és y koordináta bal oldali szomszédjának az értéke(4)
                print("Bal szomszéd értéke:", bal_szomszed)

                jobb_szomszed = my_list[y][x + 1] #az x és y koordináta jobb oldali szomszédjának az értéke(6)
                print("Jobb oldali szomszéd:", jobb_szomszed)

                felso_szomszed = my_list[y - 1][x] #az x és y koordináta felső szomszédjának az értéke(2)
                print("Felső szomszéd:", felso_szomszed)

                also_szomszed = my_list[y + 1][x] #az x és y koordináta alsó szomszédjának az értéke(8)
                print("Alsó szomszéd:", also_szomszed)

                bal_felso_szomszed = my_list[y - 1][x - 1] #az x és y koordináta bal felső szomszédjának az értéke(1)
            except(IndexError):
                pass



tablesize = int(input("choose your gamearea size:"))
my_list = []
g = []
boardsize()
board()
shoot()