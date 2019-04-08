import numpy
import networkx as nx
G=nx.read_edgelist('facebook.comnined.txt')
N=list(G.nodes())
stll=[]
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print('shortest distance between',u,'and',v,'is',l)
            stll.append(l)
            
min_spll=min(stll)
max_spll=max(stll)
avg_spll=numpy.average(spll)
print(min_spll)
print(avg_spll)
print(max_spll)

