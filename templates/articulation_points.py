TIME = 0
#dziala
class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []
        self.parent = None #rodzic w drzewie dfs
        self.discovery = 0 #czas odkrycia
        self.low = 0
        self.is_ap = False #czy jest punktem artykulacji
        self.children = 0

def dfs_visit(idx, vertices):
    global TIME
    v = vertices[idx]
    v.visited = True
    v.discovery = TIME
    v.low = TIME
    TIME += 1
    for neighbor in v.neighbors:
        if not neighbor.visited:
            neighbor.parent = v
            v.children += 1
            dfs_visit(neighbor.idx, vertices)
            v.low = min(v.low, neighbor.low) #czy jest krawedz wsteczna
            if v.parent is None and v.children > 1: #jesli to jest korzen i ma co najmniej dwojke dzieci
                v.is_ap = True
            if v.parent is not None and neighbor.low >= v.discovery:
                v.is_ap = True
        elif v.parent != neighbor:
            v.low = min(v.low, neighbor.discovery)

def find_ap(G):
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

    for v in vertices:
        if not v.visited:
            dfs_visit(v.idx, vertices)

    for v in vertices:
        if v.is_ap:
            print(v.idx)

G1 = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], 
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

find_ap(G1) #3, 6, 10

G2 = [
    [0, 1, 1, 1, 0], 
    [1, 0, 1, 0, 0], 
    [1, 1, 0, 0, 0], 
    [1, 0, 0, 0, 1], 
    [0, 0, 0, 1, 0] 
]

find_ap(G2) #0, 3