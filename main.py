import networkx as nx
import matplotlib.pyplot as plt
import readFile

network,user,service=readFile.getNetwork()
a=nx.spring_layout(network)
nx.draw_networkx_edge_labels(network,pos=a)
nx.draw_networkx(network,pos=a,with_labels=True)
plt.show()