import gambarnode as gmbr

def openfile(namafile):
    file = open(namafile)
    r = file.read()
    seplit = r.split()
    return seplit

def atr_nodes(file_read_split):
    jumlah_node = int(file_read_split[0])
    g = {}
    for i in range(jumlah_node):
        posisi_node = i * 3 + 1
        node = file_read_split[posisi_node]
        g[node] = {}
        g[node]["lat"] = file_read_split[int(posisi_node+1)]
        g[node]["long"] = file_read_split[int(posisi_node + 2)]
    return g

def list_nodes(file_read_split):
    jumlah_node = int(file_read_split[0])
    node_list = []

    for i in range(jumlah_node):
        posisi_node = i*3+1
        node_list.append(file_read_split[posisi_node])
    return node_list


def matriks_ketetangaan_to_edge(file_read_split, list_of_nodes):
    list_edge = []
    jumlah_node = int(file_read_split[0])
    initial_index_matriks = jumlah_node*3+1
    for j in range(initial_index_matriks,len(file_read_split)):
        x = (j-1) // jumlah_node - 3
        y = (j-1) % jumlah_node
        edge = ()
        temp = list(edge)
        if int(file_read_split[j]):
            temp.append(list_of_nodes[x])
            temp.append(list_of_nodes[y])
            edge = tuple(temp)
            list_edge.append(edge)

    return list_edge

def jarakeuclidian(init,dest,dict_atr_node):
    y1 = float(dict_atr_node[init]["long"])
    x2 = float(dict_atr_node[dest]["lat"])
    y2 = float(dict_atr_node[dest]["long"])
    x1 = float(dict_atr_node[init]["lat"])

    latlangToKM = 111.319

    count = (((x2-x1)**2 + (y2-y1)**2)**0.5) * latlangToKM

    return count

def bobot_edge(list_edge,dict_atr_node):
    bobot=[]
    for i in range(len(list_edge)):
        temp = jarakeuclidian(list_edge[i][0],list_edge[i][1],dict_atr_node)
        bobot.append(temp)
    return bobot

def getTetangga(init,list_edges):
    temp = []
    for i in range(len(list_edges)):
        if(list_edges[i][0] == init):
            temp.append(list_edges[i][1])
    return temp

def getbobotadj (namasimpul, list_edges, atr):
    matbobot = []
    adj = getTetangga(namasimpul,list_edges)
    for i in range (len(adj)):
        matbobot.append(jarakeuclidian(namasimpul, adj[i],atr))
    return matbobot

def adjplusbobot(adj,bobotadj):
    dict = {}
    for i in range(len(adj)):
        dict[adj[i]] = bobotadj[i]
    new = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    return new

def arah(hasil):
    tempppp = []
    for i in range(len(hasil)):
        edge = ()
        temp = list(edge)
        if i > 0:
            temp.append(hasil[i - 1])
            temp.append(hasil[i])

            edge = tuple(temp)
            tempppp.append(edge)
    for j in range(len(hasil)-1,0,-1):
        edge = ()
        temp = list(edge)

        temp.append(hasil[j])
        temp.append(hasil[j-1])

        edge = tuple(temp)
        tempppp.append(edge)
    return tempppp
if __name__ == '__main__':
    file = openfile("tes.txt")
    listnodes = list_nodes(file)
    a = matriks_ketetangaan_to_edge(file,listnodes)
    atr = atr_nodes(file)
    jarak = jarakeuclidian(listnodes[0],listnodes[1],atr)
    bobot = bobot_edge(a,atr)
    # print("panjang bobot: ", len(bobot))
    # print(bobot)

    # print(jarak*1000)
    # gmbr.gambar(a,bobot)
    # print(file)
    # print(listnodes)
    # print(atr)
    # print("panjang pasangan: ", len(a))
    # print(a)
    # j = 0
    # temp = list(a)
    for i in range(len(listnodes)):
        print(listnodes[i])

    init = str(input("Masukkan Simpul Awal : "))
    dest = str(input("Masukkan Simpul Akhir : "))

    # ALGORITMA A*
    openlist = []
    closedlist = []
    ketemu = False
    cur = init
    g = 0
    h = jarakeuclidian(init,dest,atr)
    f = g + h
    closedlist.append(init)
    while(not(ketemu)):
        ttg = getTetangga(cur, a)
        bobot_ttg = getbobotadj(cur,a,atr)
        dict = adjplusbobot(ttg,bobot_ttg)
        for i in range(len(ttg)):
            g = 0
            temp = 0
            openlist.append(ttg[i])

            tes = dict[ttg[i]] + g
            g = tes
            h = jarakeuclidian(ttg[i],dest,atr)
            f = g + h
            openlist.append(f)
            openlist.append(g)
            openlist.append(h)

        for i in range(len(openlist)):
            y = i % 4
            if y == 0:
                if openlist[i] == dest:
                    ketemu = True
                    closedlist.append(dest)
                    break

        idx =0
        kecil = 999999
        pjg = len(openlist)
        for i in range(pjg):
            x = i%4
            if(x == 1):
                if(kecil > openlist[i]):
                    kecil = openlist[i]

        idx = openlist.index(kecil)
        cur = openlist[idx-1]
        if (not(ketemu)):
            closedlist.append(cur)

    print(closedlist)
    hasil = arah(closedlist)
    print(a)
    print(hasil)
    gmbr.gambar(a,hasil,bobot)