#dziala
class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []
        self.t_neighbors = []

def dfs_visit(idx, vertices, s): #pierwsze przejscie dfs
    v = vertices[idx]
    v.visited = True
    for neighbor in v.neighbors:
            if not neighbor.visited:
                dfs_visit(neighbor.idx, vertices, s)
    s.append(v) #dodaje po przetworzeniu

def dfs_visit_t(idx, vertices, s): #drugie przejscie na odwroconych krawedziach
    v = vertices[idx]
    v.visited = True
    s.append(v)
    for t_neighbor in v.t_neighbors:
            if not t_neighbor.visited:
                dfs_visit_t(t_neighbor.idx, vertices, s)

def scc(G):
    vertices = []
    n = len(G)

    for i in range(n): #init wierzcholkow
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init krawedzi
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])

    s = [] #stos, do ktorego dodaje wierzcholki w kolejnosci konca przetwarzania

    for i in range(n): #dfs dla kazdego wierzcholka
        if not vertices[i].visited:
            dfs_visit(i, vertices, s)

    for v in vertices: #odwracam krawedzie
        v.visited = False #zeby jeszcze raz przejsc dfsem
        for neighbor in v.neighbors:
            neighbor.t_neighbors.append(v)

    s1 = []

    while len(s) > 0: #dopoki stos nie jest pusty
        v = s.pop()
        if not v.visited:
            dfs_visit_t(v.idx, vertices, s1)
            while len(s1) > 0:
                v1 = s1.pop()
                print(v1.idx)
            print("----")

G1 = [
    [0, 0, 1, 1, 0], 
    [1, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0] 
]

scc(G1)