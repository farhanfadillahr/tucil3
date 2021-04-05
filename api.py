file = open("tes.txt")
r = file.read()
x = r.split()

jumlah_node = int(x[0])
g ={}
node_list = []
for i in range(jumlah_node):
    posisi_node = i*3+1
    node_list.append(x[posisi_node])
    node = x[posisi_node]
    g[node] = {}
    g[node]["lat"] = x[int(posisi_node+1)]
    g[node]["long"] = x[int(posisi_node + 2)]

    print(x[posisi_node])

print(x)