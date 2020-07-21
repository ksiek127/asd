from collections import deque
#dziala
class Node():
    def __init__(self):
        self.idx = None
        self.visited = False
        self.neighbors = []

def dfs_visit(idx, vertices, s):
    v = vertices[idx]
    v.visited = True
    for neighbor in v.neighbors:
        if not neighbor.visited:
            dfs_visit(neighbor.idx, vertices, s)
    s.append(v)

def topological_sort(DAG):
    vertices = []
    n = len(DAG)

    for i in range(n): #init vertices
        v = Node()
        v.idx = i
        vertices.append(v)

    for i in range(n): #init edges
        for j in range(n):
            if DAG[i][j] == 1:
                vertices[i].neighbors.append(vertices[j])

    s = deque()
    idx = 0
    while idx < n:
        if not vertices[idx].visited:
            dfs_visit(idx, vertices, s)
        idx += 1

    return s

G1 = [
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0 ],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0 ],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] 

]

t_sorted = topological_sort(G1)
for i in range(len(t_sorted) - 1, -1, -1):
    print(t_sorted[i].idx)