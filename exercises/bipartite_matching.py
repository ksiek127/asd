class Node(): #dziala
    def __init__(self, idx):
        self.idx = idx
        self.visited = False
        self.neighbors = []
        self.parent = None #parent do maksymalnego przeplywu

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

def connect_source_sink(G, source, sink, v, is_source):
    v.visited = True
    if is_source:
        for neighbor in v.neighbors:
            if not neighbor.visited:
                source.neighbors.append(v) #lacze zrodlo z wierzcholkiem
                G[source.idx][neighbor.idx] = 1 #aktualizuje macierz sasiedztwa
                connect_source_sink(G, source, sink, neighbor, False)
    else:
        for neighbor in v.neighbors:
            if not neighbor.visited:
                neighbor.neighbors.append(sink) #lacze wierzcholek z ujsciem
                G[neighbor.idx][sink.idx] = 1 #aktualizuje macierz
                connect_source_sink(G, source, sink, neighbor, True)

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
    
    #wypisuje krawedzie, ktore mialy wagi, a teraz maja wage rowna 0 (poza sztucznym zrodlem i ujsciem)
    for i in range(n-2):
        for j in range(n-2):
            if G[i][j] == 0 and original_graph[i][j] != 0:
                print(i, j)

def matching(G):
    vertices = []
    n = len(G)
    G.append([0] * n) #dodaje zrodlo i ujscie
    G.append([0] * n)
    n += 2
    for i in range(n):
        G[i].append(0)
        G[i].append(0)
    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        vertices.append(v)

    for i in range(n - 2): #wczytuje krawedzie
        for j in range(n - 2):
            if G[i][j] != 0:
                vertices[i].neighbors.append(vertices[j])

    vertices[n-2].visited = True
    vertices[n-1].visited = True
    G[n-2][0] = 1 #lacze zrodlo z pierwszym wierzcholkiem
    vertices[n-2].neighbors.append(vertices[0])
    connect_source_sink(G, vertices[n-2], vertices[n-1], vertices[0], False) #lacze zrodlo z 'lewa' czescia grafu dwudzielnego, a 'prawa' lacze z ujsciem

    for v in vertices:
        v.visited = False #resetuje pole visited przed szukaniem sciezki powiekszajacej

    min_cut(G, n-2, n-1)

graph1 = [
[0, 1, 1, 0, 0, 0, 0], 
[1, 0, 0, 1, 1, 1, 0], 
[1, 0, 0, 0, 1, 0, 0], 
[0, 1, 0, 0, 0, 0, 1], 
[0, 1, 1, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

matching(graph1)