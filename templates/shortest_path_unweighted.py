from collections import deque
#dziala
class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []
        self.d = 0

def shortest_path(G, start, end):
    vertices = []
    n = len(G)
    q = deque()
    for i in range(n): #init wierzcholkow
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init krawedzi
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])
    
    v = vertices[start]
    v.visited = True
    v.d = 0
    q.appendleft(v)
    while q:
        v = q.pop()
        if v.idx == end:
            return v.d
        for neigh in v.neighbors:
            if not neigh.visited:
                neigh.visited = True
                neigh.d = v.d + 1
                q.appendleft(neigh)
    return -1 #sciezka nie istnieje

G1 = [
    [0, 1, 1, 0, 0, 0, 1, 0], 
    [1, 0, 0, 0, 0, 1, 0, 0], 
    [1, 0, 0, 1, 0, 0, 1, 0], 
    [0, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 0, 1, 0, 1, 1, 1], 
    [0, 1, 0, 0, 1, 0, 0, 0], 
    [1, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0], 
]

print(shortest_path(G1, 0, 7))