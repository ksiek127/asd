#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.d = float('inf')
        self.neighbors = []

def relax(dist, u, v):
    if v.d > u.d + dist: #dist to waga krawedzi u-v
        v.d = u.d + dist

def is_negative_cycle(edges):
    for e in edges: #dla kazdej krawedzi
        if e[1].d > e[0].d + e[2]: #jesli istnieje krotsza sciezka niz ta, ktora znalazl algorytm, to jest ujemny cykl
            return True
    return False

def shortest_paths(G, source):
    n = len(G)
    vertices = []
    edges = []
    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        vertices.append(v)
    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                vertices[i].neighbors.append((vertices[j], G[i][j]))
                edges.append((vertices[i], vertices[j], G[i][j]))
    vertices[source].d = 0
    for i in range(n - 1): #relaksacja wszystkich krawedzi n-1 razy
        for e in edges:
            relax(e[2], e[0], e[1])

    if is_negative_cycle(edges): #jesli jest ujemny cykl, algorytm nie dziala
        print("ujemny cykl")
    else:
        for v in vertices: #wypisuje odleglosci od zrodla, jesli nie ma ujemnego cyklu
            print(v.idx, v.d)

G1 = [
    [0, 0, 0, 0, 3, 0, 0, 0, 0], 
[5, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 3, 7, 0, 42, 5, 1, 0, 11], 
[0, 0, 0, 0, 0, 0, 5, 0, 0], 
[0, 0, 3, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 3, 0]
]

G2 = [
    [0, 0, 0, 0, 3, 0, 0, 0, 0], 
[5, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 3, 7, 0, 42, 5, 1, 0, 11], 
[0, 0, 0, 0, 0, 0, 5, 0, 0], 
[0, 0, 3, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, -50, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 3, 0]
]

G3 = [
    [0, 0, 0, 0, -3, 0, 0, 0, 0], 
[-5, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 3, 7, 0, -42, 5, 1, 0, -11], 
[0, 0, 0, 0, 0, 0, 5, 0, 0], 
[0, 0, -3, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 3, 0]
]

shortest_paths(G1, 3) #ok
print("------------------------")
shortest_paths(G2, 3) #ujemny cykl, dziala
print("------------------------")
shortest_paths(G3, 3) #ok