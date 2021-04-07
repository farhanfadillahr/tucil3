import networkx as nx
import matplotlib.pyplot as plt

def gambarjadi(edge,hasill,bobot):
    G = nx.DiGraph()
    for i in range(len(edge)):
        G.add_edges_from([edge[i]], weight = '{:.2f}'.format(bobot[i]*1000))

    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    # Specify the edges you want here
    red_edges = hasill
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                            node_size = 600)

    nx.draw_networkx_labels(G, pos, font_size=5,horizontalalignment='center')
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    fig = plt.gcf()
    fig.set_size_inches(8,8)
    plt.show()

def gambar(edge,bobot):
    G = nx.DiGraph()
    for i in range(len(edge)):
        G.add_edges_from([edge[i]], weight = '{:.2f}'.format(bobot[i]*1000))
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    black_edges = edge
    edge_colours = ['' if not edge in black_edges else 'black'
                    for edge in G.edges()]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                            node_size = 1500)
    nx.draw_networkx_labels(G, pos, font_size=6,horizontalalignment='center')
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    fig = plt.gcf()
    fig.set_size_inches(8,8)
    plt.show()