class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []

def dfs_visit(idx, vertices):
    v = vertices[idx]
    v.visited = True
    print(v.idx)
    for neighbor in v.neighbors:
        if not neighbor.visited:
            dfs_visit(neighbor.idx, vertices)

def dfs(G, idx):
    vertices = []
    n = len(G)

    for i in range(n): #wczytuje wierzcholki
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])

    dfs_visit(idx, vertices)

G1 = [
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

dfs(G1, 1)