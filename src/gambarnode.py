import networkx as nx
import matplotlib.pyplot as plt

def gambar(edge,hasill,bobot):
    G = nx.DiGraph()
    for i in range(len(edge)):
        G.add_edges_from([edge[i]], weight = '{:.2f}'.format(bobot[i]*1000))

    # values = [val_map.get(node, 0.25) for node in G.nodes()]
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    # Specify the edges you want here
    red_edges = hasill
    edge_colours = ['black' if not edge in red_edges else 'red'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]
    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                            node_size = 1500)
    # nx.draw(G, pos=pos,node_color='orange',
    #         with_labels=False,
    #         node_size=600)
    # for node, (x, y) in pos.items():
    #     plt.text(x, y, node, fontsize=5, ha='center', va='center')
    nx.draw_networkx_labels(G, pos, font_size=6,horizontalalignment='center')
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()