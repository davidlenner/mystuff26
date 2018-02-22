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

#def shoot():
 #   for i in range(0,len(my_list)):
 #       for t in range(0,len(my_list)):


tablesize = int(input("choose your gamearea size:"))
my_list = []
g = []
boardsize()
board()