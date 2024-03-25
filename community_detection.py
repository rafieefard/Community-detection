
import igraph as ig
from igraph import *
from itertools import combinations


keywords = Graph.Read_GraphML('all_irandoc_label_same_name.graphml')
keywords.vs.select(_degree=0).delete()
keywords.vs.select(_degree=1).delete()
print(keywords.summary())
cliques = keywords.maximal_cliques(min=3)
print("len cliques is:",len(cliques))
print('Found {} maxial cliques having sizes:'.format(len(cliques)))

def cliqsBySize(cliques):
    cqsizes = {}
    for cx in cliques:
        cxsz = len(cx)  # Size of the clique
        cqsizes[cxsz] = cqsizes.get(cxsz, 0) + 1
    return cqsizes
print(cliqsBySize(cliques))
nodes=[]
for clique in cliques:
    for node in clique:
        if node not in nodes:
            nodes.append(node)
            break
print(len(nodes))
cliques_graph=Graph.subgraph(keywords,nodes)
print("cliques_graph summary is:",cliques_graph.summary())
cliques_graph.vs.select(_degree=0).delete()
cliques_graph.vs.select(_degree=1).delete()
print("cliques_graph summary after delete node 0 and 1 is:",cliques_graph.summary())
degree = keywords.degree()
visual_style =  {}
visual_style["vertex_size"] = [int(x)+20 for x in degree]
visual_style["bbox"] = (2400, 1800)
visual_style["margin"] = 100
visual_style["vertex_label"] = ""

visual_style["layout"] = keywords.layout_fruchterman_reingold()
visual_style['mark_groups'] = True
cliques_graph.write_graphml('cliques_graph.graphml')
ig.plot(cliques_graph)
for i in range(0,10):
    seq = keywords.vs.select(cliques[i])
    subg = seq.subgraph()
    subg.vs["label"] = subg.vs["name"]
    subg.vs['color'] = 'green'
ig.plot(subg)