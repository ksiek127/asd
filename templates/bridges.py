TIME = 0
#dziala
class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []
        self.discovery = 0
        self.low = 0
        self.parent = None

def dfs_visit(idx, vertices):
    global TIME
    v = vertices[idx]
    v.visited = True
    v.discovery = TIME #poczatkowe wartosci czasu odkrycia i low
    v.low = TIME
    TIME += 1
    for neighbor in v.neighbors:
        if not neighbor.visited:
            neighbor.parent = v
            dfs_visit(neighbor.idx, vertices)
            v.low = min(v.low, neighbor.low) #czy istnieje krawedz wsteczna od potomka v do jego przodka
            if neighbor.low > v.discovery: #v-neighbor to most
                print(v.idx, neighbor.idx)

        elif neighbor != v.parent:
            v.low = min(v.low, neighbor.discovery)

def bridge(G):
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

    for i in range(n):
        if not vertices[i].visited:
            dfs_visit(i, vertices)

G1 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 1, 1, 0], 
[0, 0, 0, 1, 1, 1, 0, 0, 1], 
[0, 0, 1, 0, 1, 0, 0, 0, 0], 
[0, 0, 1, 1, 0, 1, 0, 0, 0], 
[0, 0, 1, 0, 1, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0, 1, 0], 
[0, 1, 0, 0, 0, 0, 1, 0, 1], 
[0, 0, 1, 0, 0, 0, 0, 1, 0]
]

bridge(G1) # 0-1, 2-8, 7-8