from Structure_Extractor import extractor
from graph_builder import builder
import networkx as nx
import matplotlib.pyplot as plt


def renderer(graph,edge_labels): 
    if not graph.nodes:
        print("graph is empty")
        return
    max_len = max(len(str(node)) for node in graph.nodes)
    base = 300
    nodes_sizes = [len(str(node)) ** 2 * 45 for node in graph.nodes]    
    pos = nx.spring_layout(graph)
    draw = nx.draw(graph,pos, with_labels = True, node_size=nodes_sizes )
    etiquette = nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)
    show = plt.show()
    return show
    
