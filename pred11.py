from math import *
from queue import *

def dijkstra(G, s, e, P):
    #Dijkstra, search for the nearest path
    d = [inf] * (len(G) + 1)

    #Priority queue
    PQ = PriorityQueue()

    #Add starting node
    PQ.put((0, s))
    d[s] = 0

    #Until PQ is empty
    while not PQ.empty():
        #Get node with lowest priority
        du, u = PQ.get()

        #Browse its neeighbors
        for v, wuv in G[u].items():
            #Relax
            if d[v] > d[u] + wuv:
                d[v] = d[u] + wuv
                P[v] = u

                #Add v to PQ
                PQ.put((d[v], v))
    return d[e]


def recPath(u, v, P):
    path = []

    #Repeat unit we reach u
    while v != u and v != None:
        path.append(v)
        v = P[v]

    path.append(u)

    return path

G = {
    1 : {2:8, 3:4, 5:2},
    2 : {1:8, 3:5, 4:2, 7:6, 8:7},
    3 : {1:4, 2:5, 6:3, 7:4},
    4 : {2:2, 9:3},
    5 : {1:2, 6:5},
    6 : {3:3, 5:5, 7:5, 8:7, 9:10},
    7 : {2:6, 3:4, 6:5, 8:3},
    8 : {2:7, 6:7, 7:3, 9:1},
    9 : {4:3, 6:10, 8:1}
}

#Dijkstra method
P = [None] * (len(G) + 1)
dist = dijkstra(G, 1, 9, P)
path = recPath(1, 9, P)
print(path)
print(dist)