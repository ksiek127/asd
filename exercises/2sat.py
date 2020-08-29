#dziala
class Node():
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.neighbors = []
        self.t_neighbors = []

def dfs_visit(v, s): #pierwsze przejscie dfs
    v.visited = True
    for neighbor in v.neighbors:
            if not neighbor.visited:
                dfs_visit(neighbor, s)
    s.append(v) #dodaje po przetworzeniu

def dfs_visit_t(v, s): #drugie przejscie na odwroconych krawedziach
    v.visited = True
    s.append(v)
    for t_neighbor in v.t_neighbors:
            if not t_neighbor.visited:
                dfs_visit_t(t_neighbor, s)

def negation(x): #zanegowana zmienna x
    if len(x) == 1: #jesli nie ma zaprzeczenia
        return '~' + x
    else: #jesli ma zaprzeczenie
        return x[1]

def get_idx(variables, x): #zwraca indeks zmiennej x
    k = 0
    while variables[k] != x: #zakladam, ze zmienna jest w liscie zmiennych
        k += 1
    return k

def is_satisfiable(variables, formula):
    vertices = []
    n = len(variables)
    for i in range(n): #wczytuje wierzcholki
        v = Node(variables[i])
        vertices.append(v)
    for clause in formula: #wczytuje krawedzie
        # x v y <=> (~x => y) and (~y => x)
        vertices[get_idx(variables, negation(clause[0]))].neighbors.append(vertices[get_idx(variables, clause[1])])
        vertices[get_idx(variables, negation(clause[1]))].neighbors.append(vertices[get_idx(variables, clause[0])])
    
    s = [] #stos, do ktorego dodaje wierzcholki w kolejnosci konca przetwarzania

    for i in range(n): #dfs dla kazdego wierzcholka
        if not vertices[i].visited:
            dfs_visit(vertices[i], s)

    for v in vertices: #odwracam krawedzie
        v.visited = False #zeby jeszcze raz przejsc dfsem
        for neighbor in v.neighbors:
            neighbor.t_neighbors.append(v)

    s1 = []

    while len(s) > 0: #dopoki stos nie jest pusty
        v = s.pop()
        if not v.visited:
            dfs_visit_t(v, s1)
            curr_cycle = []
            while len(s1):
                u = s1.pop()
                curr_cycle.append(u.val)
            for x in curr_cycle:
                if negation(x) in curr_cycle: #jesli zmienna i jej negacja leza na cyklu, to formula jest niespelnialna
                    return False
    return True

variables1 = ['x', '~x', 'y', '~y', 'z', '~z']
formula1 = [
    ['x', 'y'],
    ['~x', 'z'],
    ['~x', 'y'],
    ['~z', '~y']
]

print(is_satisfiable(variables1, formula1))