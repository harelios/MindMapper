import networkx as nx 
from Structure_Extractor import extractor
import matplotlib.pyplot as plt


def builder(dictio):
    graph = nx.DiGraph()
    data = dictio
    edge_labels = {}
    for sujet,relations in data.items():
        for connecteur,valeurs in relations.items():
            for element in valeurs:
                graph.add_edge(sujet,element,label=connecteur)
                for u,v,d in graph.edges(data=True):
                    if "label" in d :
                        edge_labels[(u,v)] = d["label"]
    return graph,edge_labels
    
