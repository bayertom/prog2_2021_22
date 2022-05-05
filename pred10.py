def BFS(G, u, P):
    #All nodes are new
    S = ['N'] *  (len(G) + 1)

    #Create queue
    Q = []

    #Add starting node and change status
    Q.append(u)
    S[u] = 'O'

    #Until Q is empty
    while Q:
        #Take fist node
        u = Q.pop(0)

        #Browse its neighbors
        for v in G[u]:
            if S[v] == 'N':

                #Change its status
                S[v] = 'O'

                #Remember itd predecessor
                P[v] = u

                #Add v to Q
                Q.append(v)

        #U is closed
        S[u] = 'C'

def recPath(u, v, P):
    path = []

    #Repeat unit we reach u
    while v != u and v != None:
        path.append(v)
        v = P[v]

    path.append(u)

    return path

def DFS(G, u, P):
    #All nodes are new
    S = ['N'] *  (len(G) + 1)
    DFSR(G, S, P, u)

def DFSR(G, S, P, u):
    #Change status
    S[u] = 'O'

    #Browse its neighbors
    for v in G[u]:
        #Only new nodes
        if S[v] == 'N':
            #Remeber its predecessor
            P[v] = u

            #REcursive call
            DFSR(G, S, P, v)

    #Close node
    S[u] = 'C'


G = {
    1 : [2, 3, 5],
    2 : [1, 3, 4, 7, 8],
    3 : [1, 2, 6, 7],
    4 : [2, 9],
    5 : [1, 6],
    6 : [3, 5, 7, 8, 9],
    7 : [2, 3, 6, 8],
    8 : [2, 6, 7, 9],
    9 : [4, 6, 8]
}

#BFS + DFS
P = [None] * (len(G) + 1)
DFS(G, 1, P)
print(P)
path = recPath(1, 9, P)

print(path)


