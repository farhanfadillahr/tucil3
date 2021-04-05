import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('SimpangTuguAsiaAfrika', 'B'), ('SimpangTuguAsiaAfrika', 'C'), ('B', 'D'), ('C', 'D')])
print(G)
val_map = {'A': 1.0,
           'B': 2.0,
           'C': 3.0,
           'D': 5.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('SimpangTuguAsiaAfrika', 'B'), ('SimpangTuguAsiaAfrika', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]
list(G.edges)
list(G.nodes)
# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                        node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
plt.show()