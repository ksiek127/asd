#chyba dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.neighbors = []

def shortest_paths(G):
    n = len(G)
    vertices = []
    distances = [None] * n #tablica odleglosci
    for i in range(n):
        distances[i] = [0] * n
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                distances[i][j] = G[i][j]
            else:
                distances[i][j] = float('inf')
    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        vertices.append(v)
    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                vertices[i].neighbors.append((vertices[j], G[i][j]))

    for k in range(n):
        for i in range(n): #dla kazdego wierzcholka
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    for i in range(n):
        print(distances[i])

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

shortest_paths(G1)