from collections import deque

class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []
        self.d = 0
        self.part = 0

def shortest_path(G, start, end): #graf skierowany
    vertices = []
    n = len(G)
    q = deque()
    for i in range(n): #init wierzcholkow
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init krawedzi
        for j in range(n):
            if G[i][j] != 0: #jesli jest krawedz
                vertices[i].neighbors.append((vertices[j], G[i][j])) #(wierzcholek, waga krawedzi)
    
    v = vertices[start]
    v.visited = True
    v.d = 0
    q.appendleft(v)
    while q:
        v = q.pop()
        if v.part != 0: #jesli to jest sztucznie dodany wierzcholek
            v.d += 1
            v.part -= 1
            q.appendleft(v)
        else: #jesli to jest 'normalny' wierzcholek
            if v.idx == end:
                return v.d
            v.visited = True
            for neigh in v.neighbors: #dodaje nieodwiedzonych sasiadow do kolejki
                if not neigh[0].visited:
                    # neigh[0].visited = True
                    neigh[0].d = v.d
                    neigh[0].part = neigh[1]
                    q.appendleft(neigh[0])
    return -1 #sciezka nie istnieje

G1 = [
    [0, 3, 5, 5, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 5, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 3], 
    [0, 0, 0, 0, 0, 0, 3, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 7, 0] 
]

print(shortest_path(G1, 0, 6)) #9
print(shortest_path(G1, 0, 7)) #7