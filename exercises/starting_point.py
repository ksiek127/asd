class Node(): #powinno dzialac
    def __init__(self, idx):
        self.idx = idx
        self.visited = False
        self.neighbors = []

def dfs_visit(v, path):
    path.append(v)
    v.visited = True
    for neighbor in v.neighbors:
        if not neighbor.visited:
            dfs_visit(neighbor, path)
    return len(path)

def start(G):
    vertices = []
    n = len(G)

    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        v.idx = i
        vertices.append(v)

    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])
    for v in vertices:
        if dfs_visit(v, []) == n: #jesli przeszedlem po kazdym wierzcholku
            return v.idx
        for v in vertices:
            v.visited = False #resetuje pole visited przed kolejnym przejsciem dfs