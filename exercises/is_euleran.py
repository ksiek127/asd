class Edge():
    def __init__(self, u, v):
        self.u = u #krawedz z wierzcholka u do v
        self.v = v
        self.next = []

def euleran(edges): #graf spojny, nieskierowany
    vertices_deg = [0] * len(edges) #stopnie wierzcholkow
    for e in edges:
        vertices_deg[e.u] += 1
        vertices_deg[e.v] += 1
    for deg in vertices_deg:
        if deg % 2 == 1: #jesli jakis wierzcholek ma nieparzysty stopien
            return False
    return True