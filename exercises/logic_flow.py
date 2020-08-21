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

def assign_values(variables, formula):
    n = 2 + int(1.5 * len(variables)) + len(formula)
    G = [None] * n #buduje macierz sasiedztwa
    for i in range(n):
        G[i] = [0] * n
    for i in range(1, len(variables) // 2 + 1): #polaczenie zrodla z wierzcholkami pomocniczymi
        G[0][i] = 1
    for i in range(1, len(variables) // 2 + 1): #polaczenie wierzcholkow pomocniczych ze zmiennymi
        G[i][len(variables) // 2 + 2 * (i - 1) + 1] = 1
        G[i][len(variables) // 2 + 2 * (i - 1) + 2] = 1
    for i in range(len(formula)): #polaczenie zmiennych z klauzulami
        for j in range(len(variables)):
            if variables[j] in formula[i]: #jesli zmienna znajduje sie w klauzuli
                G[1 + len(variables) // 2 + j][1 + (int)(1.5 * len(variables)) + i] = 1
    for i in range(len(formula)): #polaczenie klauzul z ujsciem
        G[1 + (int)(1.5 * len(variables)) + i][n-1] = 1
    source = 0
    sink = n - 1

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
    variables_used = []
    for i in range(1 + len(variables) // 2, 1 + (int)(1.5 * len(variables))):
        for j in range(1 + (int)(1.5 * len(variables)), n - 1):
            if G[i][j] == 0 and original_graph[i][j] == 1: #jesli krawedz ma wage 0, a w oryginalnym grafie miala wage 1, to byl tu przeplyw i uzylem zmiennej z lewego wierzcholka tej krawedzi
                variables_used.append(variables[i - 1 - len(variables) // 2])
    return variables_used

variables1 = ['x', '~x', 'y', '~y', 'z', '~z', 'v', '~v', 'w', '~w']
formula1 = [
    ['x', 'y', 'z'], ['~y', 'w'], ['~z', 'v'], ['~x', '~w'], ['~v']
]
print(assign_values(variables1, formula1))