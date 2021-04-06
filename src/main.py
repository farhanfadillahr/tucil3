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

def getindex(nama_simpul, listnodes):
    cek = False
    i = 0
    while ((cek==False) & i != len(listnodes)):
        if(listnodes[i]==nama_simpul):
            cek = True
            return i
        else:
            i = i+1
    if(cek == False):
        return (-1)

def matttg(namafile):
    file = open(namafile, "r")
    fread = file.readlines()
    jumlah = int(fread[0])
    mat = [[0 for i in range (jumlah)] for j in range (jumlah)]
    for i in range(jumlah+1, len(fread), 1):
        fread[i] = fread[i].replace("\n", "")
        matsplit = []
        matsplit = fread[i].split(" ")
        for j in range (jumlah):
            mat[i-jumlah-1][j]=matsplit[j]
        # print('\n')
    return mat

def getadj(nama_simpul, mat, listnodes):
    idx = getindex(nama_simpul, listnodes)
    matadj = []
    for i in range (len(listnodes)):
        if(mat[idx][i]=='1'):
            matadj.append(i)
    return matadj
 

def isidxtrue(nama_simpul,nama_tujuan, listnodes):
    idx = getindex(nama_simpul,listnodes)
    idx2 = getindex(nama_tujuan, listnodes)
    if(idx != (-1) & idx2 != (-1)):
        return True
    else:
        return False
    
def getbobotsum (namasimpul, listnodes, atr, adj, tujuan):
    matbobot = []
    gn = getgn(namasimpul,listnodes, atr, adj)
    hn = gethn(namasimpul,listnodes,atr,adj)
    for i in range (len(adj)):
        matbobot.append(gn[i]+hn[i])
    return matbobot

def getgn (namasimpul, listnodes, atr, adj):
    matbobot = []
    for i in range (len(adj)):
        matbobot.append((jarakeuclidian(namasimpul, listnodes[adj[i]],atr)*10**3))
    return matbobot

def gethn(tujuan, listnodes, atr, adj):
    hn=[]
    for i in range (len(adj)):
        hn.append(jarakeuclidian(listnodes[adj[i]],tujuan,atr)*10**3)
    return hn

def sort_list(mylist,adj, mylist1):
    # outer loop
    for i in range(len(mylist)-1, 0, -1):
        # inner loop
        for j in range(i):
            if mylist1[j] > mylist1[j+1]:
                # swap the value
                temp = mylist[j]
                temp1 = adj[j]
                temp2 = mylist1[j]
                mylist[j] = mylist[j+1]
                adj[j]=adj[j+1]
                mylist1[j] = mylist1[j+1]
                mylist[j+1] = temp
                adj[j+1]=temp1
                mylist1[j+1]=temp2

def sort_f(asal, listnodes, list, atr, tujuan):
    li = []
    for i in range(len(list)):
        li.append(getindex(list[i],listnodes))
    bobotsum = getbobotsum(asal,listnodes,atr,li,tujuan)
    sort_list(li,list,bobotsum)
            

def astar (asal, tujuan, listnodes, mat, atr):
    openlist = [] 
    closedlist=[]
    openlist.append(asal)
    while(len(openlist)!=0):
        sort_f(asal,listnodes,openlist,atr,tujuan)
        curr = openlist[0]
        openlist.remove(curr)
        closedlist.append(curr)
        adjnei = getadj(curr,mat,listnodes)
        for i in range (len(adjnei)):
            if(listnodes[adjnei[i]] in closedlist):
                pass
            else :
                if(listnodes[adjnei[i]] not in closedlist):
                    openlist.append(listnodes[adjnei[i]])
        if(tujuan in openlist):
            break
    return closedlist

if __name__ == '__main__':
    dokumen = "../test/tes.txt"
    file = openfile(dokumen)
    jml = int(file[0])
    listnodes = list_nodes(file)
    a = matriks_ketetangaan_to_edge(file,listnodes)
    atr = atr_nodes(file)
    jarak = jarakeuclidian(listnodes[0],listnodes[1],atr)
    bobot = bobot_edge(a,atr)
    # print(jarak*1000)
    
    #Cek List
    for i in range (len(listnodes)):
        print (listnodes[i])

    gmbr.gambar(a,bobot)
    mat = matttg(dokumen)
    print(mat[0])
    awal = str(input("Masukkan Simpul Awal : "))
    tujuan = str(input("Masukkan Simpul Tujuan : "))
    adj = getadj(awal,mat,listnodes)
    print(len(adj))
    print(getindex(awal,listnodes))
    hasil = astar(awal,tujuan,listnodes,mat,atr)
    for i in range(len(hasil)):
        print(hasil[i])
    # print(file)
    # print(listnodes)
    # print(atr)
    # print(a)
