from collections import deque

class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []

def bfs(G, start):
    vertices = []
    n = len(G)
    q = deque()
    for i in range(n): #init vertices
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init edges
        for j in range(n):
            if G[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])
    
    v = vertices[start]
    v.visited = True
    q.appendleft(v)
    while q:
        v = q.pop()
        for neigh in v.neighbors:
            if not neigh.visited:
                neigh.visited = True
                q.appendleft(neigh)
