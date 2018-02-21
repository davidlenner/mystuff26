tablesize = int(input("gfdg:"))
while tablesize >10:
    tablesize = int(input("gfdg:"))

my_list = []
g = []


z = 0
u = tablesize

for x in range(1, (tablesize*tablesize)+1):
    g.append(x)
for i in range(tablesize):    
    my_list.append(g[z:u])
    z += tablesize
    u += tablesize
print(my_list)