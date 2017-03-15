import os
import networkx as nx

def getNetwork():
    service=set()
    user=set()
    net=nx.Graph()
    with open('case0.txt','r') as f:
        [n,e,u]=[int(x) for x in f.readline().split(' ')]
        f.readline()
        m=int(f.readline())
        f.readline()
        while f.readline()!='\r\n':
            [s,t,w,r]=[str(int(x)) for x in f.readline().split(' ')]
            service.add(s)
            service.add(t)
            net.add_nodes_from([s,t],attr='service',demand=-10000)
            net.add_edge(s,t,capacity=int(w),weight=int(r))
        lst=f.readlines()
        for y in lst:
            [u,s,r]=[str(int(x)) for x in y.split(' ')]
            user.add(u)
            net.add_node(u,attr='user',demand=int(r))
            net.add_edge(u,s,capacity=10000,weight=0)

        print (service)
        print (user)
        return net,user,service





