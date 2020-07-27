#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.visited = False
        self.neighbors = []
        self.parent = None

def is_augmenting_path(G, vertices, s, t):
    q = []
    v = vertices[s]
    v.visited = True
    q.append(v)
    while len(q):
        v = q.pop(0)
        for neighbor in v.neighbors:
            if not neighbor.visited and G[v.idx][neighbor.idx] > 0: #jesli sasiad nieodwiedzony i przeplyw na tej krawedzi jest dodatni
                neighbor.parent = v
                if neighbor.idx == t:
                    return True
                q.append(neighbor)
                neighbor.visited = True

    return False

def min_cut(G, source, sink):
    vertices = []
    n = len(G)
    max_fl = 0
    original_graph = [None] * n #pamietam wejsciowa macierz sasiedztwa, bo bedzie ona modyfikowana
    for i in range(n):
        original_graph[i] = [0] * n
    for i in range(n):
        for j in range(n):
            original_graph[i][j] = G[i][j]

    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        vertices.append(v)

    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                vertices[i].neighbors.append(vertices[j])

    while is_augmenting_path(G, vertices, source, sink): #dopoki istnieje sciezka powiekszajaca
        path_flow = float('inf')
        s = vertices[sink]
        while s.idx != source: #pojemnosc sciezki powiekszajacej to najmniejsza wartosc przeplywu w tej sciezce
            path_flow = min(path_flow, G[s.parent.idx][s.idx])
            s = s.parent
        max_fl += path_flow

        v = vertices[sink]
        while v.idx != source: #aktualizuje siec residualna
            u = v.parent
            G[u.idx][v.idx] -= path_flow
            G[v.idx][u.idx] += path_flow
            v = v.parent

        for v in vertices:
            v.visited = False #resetuje pole visited przed kolejnym przejsciem bfs w poszukiwaniu sciezki powiekszajacej
    
    #wypisuje krawedzie, ktore mialy wagi, a teraz maja wage rowna 0
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0 and original_graph[i][j] != 0:
                print(i, j)

G1 = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 

min_cut(G1, 0, 5)