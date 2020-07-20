class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []

def dfs_visit(G, start, vertices):
    vertices[start].visited = True
    print(vertices[start].idx)
    for neighbor in vertices[start].neighbors:
            if not neighbor.visited:
                dfs_visit(G, neighbor.idx, vertices)

def dfs(G, start):
    vertices = []
    n = len(G)

    for i in range(n): #init vertices
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init edges
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])

    dfs_visit(G, start, vertices)

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