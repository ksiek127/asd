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

def can_produce(factories, shops, graph):
    n = 2 + len(shops) + len(factories)
    G = [None] * n #tworze macierz sasiedztwa
    for i in range(n):
        G[i] = [0] * (n)
    for i in range(1, len(factories) + 1): #polaczenie zrodla z kazda fabryka
        G[0][i] = factories[i-1]
    for edge in graph: #polaczenie fabryk ze sklepami
        G[edge[0] + 1][edge[1] + 1 + len(factories)] = edge[2]
    for i in range(1 + len(factories), n-1): #polaczenie sklepow z ujsciem
        G[i][n-1] = shops[i - 1 - len(factories)]

    vertices = []
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
    source = 0
    sink = n-1
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
    
    for s in shops:
        max_fl -= s
    if max_fl == 0:
        return True
    return False


graph1 = [
    [0, 0, 2], [1, 0, 3], [2, 1, 3], [3, 2, 7]
] #[fabryka, sklep, przepustowosc]
factories1 = [3, 2, 4, 9]
shops1 = [4, 7, 5]
print(can_produce(factories1, shops1, graph1))