tablesize = int(input("gfdg:"))


my_list = []
g = []


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
    for y in range(0, len(my_list)):
        sor_string = " "
        for x in range(0, len(my_list[y])):
            sor_string += str("%3s" % my_list[y][x]) + " "
        print(sor_string)
 

boardsize()
board()