#dziala
class Node():
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent #korzen ma ustawione pole parent na samego siebie

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x #przylaczam mniejsze drzewo do wiekszego
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def mst(G): #dla nieskierowanego
    vertices = []
    edges = []
    n = len(G)

    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        v.parent = v
        vertices.append(v)

    for i in range(n): #wczytuje krawedzie
        for j in range(i, n):
            if G[i][j] != 0:
                # vertices[i].neighbors.append(vertices[j])
                edges.append((i, j, G[i][j]))

    edges.sort(key = lambda x: x[2]) #sortuje krawedzie
    mst_edges = [] #krawedzie, ktore tworza mst
    for i in range(len(edges)): #przegladam krawedzie w kolejnosci rosnacych wag
        v1 = vertices[edges[i][0]]
        v2 = vertices[edges[i][1]]
        if find_set(v1) != find_set(v2): #jesli wierzcholki na koncach krawedzi sa w roznych zbiorach, to dodanie tej krawedzi nie tworzy cyklu
            union(v1, v2) #unia wierzcholkow polaczonych krawedzia
            mst_edges.append(edges[i])
    
    for e in mst_edges:
        print(e[0], e[1])
        
    
G1 = [
    [0, 1, 0, 11, 5, 0, 0], 
    [1, 0, 0, 5, 0, 0, 0], 
    [0, 0, 0, 0, 0, 11, 0], 
    [11, 5, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 42, 3], 
    [0, 0, 11, 0, 42, 0, 7], 
    [0, 0, 0, 0, 3, 7, 0]
]

mst(G1)