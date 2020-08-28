#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.c = 0 #pojemnosc
        self.pos = None
        self.neighbors = []

def parent(i): #zwraca indeks rodzica
        return (i-1) // 2

def left_child(i): #indeks lewego dziecka
        return 2 * i + 1

def right_child(i): #indeks prawego dziecka
        return 2 * i + 2

def heapify(heap, i, n): #funkcja heapify dla poddrzewa ktorego korzen jest pod indeksem i
    largest = i #indeks najwiekszego elementu
    l = left_child(i)
    r = right_child(i)
    if l < n and heap[l].c > heap[i].c: #jesli istnieje lewe dziecko i ma wieksza wartosc niz root
        largest = l
    if r < n and heap[r].c > heap[largest].c: #to samo dla prawego dziecka
        largest = r
    
    if largest != i: #jesli najwieksza wartosc nie jest w korzeniu, zmieniam korzen
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest, n)

def get_max(heap, size):
    root = heap[0]
    heap[0].pos = size - 1
    heap[size - 1].pos = 0
    heap[0] = heap[size - 1]
    heapify(heap, 0, size)
    return root

def update_pos(heap, v):
    i = v.pos
    while i > 0 and heap[i].c > heap[parent(i)].c:
        heap[i].pos = parent(i)
        heap[parent(i)].pos = i
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def relax(capacity, heap, u, v):
    if v.c < min(u.c, capacity):
        v.c = min(u.c, capacity)
        update_pos(heap, v) #aktualizacja kolejki priorytetowej

def shortest_path(G, source, destiny):
    n = len(G)
    vertices = []
    q = []
    size = n
    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        vertices.append(v)
        q.append(v)
        v.pos = i #miejsce w kolejce priorytetowej
    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                vertices[i].neighbors.append((vertices[j], G[i][j]))
    v = vertices[source]
    v.c = float('inf')
    update_pos(q, v)
    while size:
        u = get_max(q, size)
        size -= 1
        for neighbor in u.neighbors:
            v = neighbor[0]
            relax(neighbor[1], q, u, v)
    return vertices[destiny].c

graph1 = [
[0, 7, 0, 0, 0, 0, 0, 10], 
[7, 0, 5, 0, 0, 0, 0, 0], 
[0, 5, 0, 3, 0, 42, 0, 0], 
[0, 0, 3, 0, 0, 42, 0, 0], 
[0, 0, 0, 0, 0, 0, 11, 7], 
[0, 0, 42, 42, 0, 0, 0, 0], 
[0, 0, 0, 0, 11, 0, 0, 42], 
[10, 0, 0, 0, 7, 0, 42, 0]
]

print(shortest_path(graph1, 6, 5))