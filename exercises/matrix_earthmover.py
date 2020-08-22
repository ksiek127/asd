class Node(): #dziala
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
    
    nr_of_moves = 0
    #wynik to roznica pomiedzy poczatkowym przeplywem miedzy wierzcholkami a aktualnym
    for i in range(n - 2):
        for j in range(i, n - 2):
            if G[i][j] != original_graph[i][j]:
                nr_of_moves += abs(G[i][j] - original_graph[i][j])
    return nr_of_moves

def min_steps(m1, m2): #zamieniam macierz1 w macierz2
    n1 = len(m1)
    T = 0 #suma wartosci pol w m1
    for i in range(n1):
        for j in range(n1):
            T += m1[i][j]
    size = n1 * n1 + 2
    G = [None] * size #tworze macierz sasiedztwa
    for i in range(size):
        G[i] = [0] * size
    for i in range(size - 2): #lacze zrodlo z wierzcholkami
        G[size-2][i] = m1[i // n1][i % n1]
    for i in range(size - 2): #lacze wierzcholki z ujsciem
        G[i][size-1] = m2[i // n1][i % n1]
    for i in range(size - 2): #lacze wierzcholki miedzy soba
        if i % n1 > 0:
            G[i][i-1] = T
        if i % n1 < n1 - 1:
            G[i][i+1] = T
        if i // n1 > 0:
            G[i][i - n1] = T
        if i // n1 < n1 - 1:
            G[i][i + n1] = T
    return min_cut(G, size - 2, size - 1)

matrix1 = [
    [4, 2, 1],
    [1, 3, 3],
    [7, 4, 8]
]

matrix2 = [
    [8, 2, 1],
    [1, 3, 5],
    [1, 7, 5]
]

print(min_steps(matrix1, matrix2))