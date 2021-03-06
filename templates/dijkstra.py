#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.d = float('inf')
        self.pos = None
        self.neighbors = []

def parent(i): #zwraca indeks rodzica
        return (i-1) // 2

def left_child(i): #indeks lewego dziecka
        return 2 * i + 1

def right_child(i): #indeks prawego dziecka
        return 2 * i + 2

def heapify(heap, i, size):
    smallest = i #najmniejszy element sposrod korzenia, lewego i prawego dziecka
    left = left_child(i)
    right = right_child(i)
    if left < size and heap[left].d < heap[smallest].d:
        smallest = left
    if right < size and heap[right].d < heap[smallest].d:
        smallest = right
    if smallest != i: #jesli ktores dziecko jest mniejsze od rodzica
        heap[smallest].pos = i
        heap[i].pos = smallest
        heap[smallest], heap[i] = heap[i], heap[smallest]
        heapify(heap, smallest, size)

def get_min(heap, size):
    root = heap[0]
    heap[0].pos = size - 1
    heap[size - 1].pos = 0
    heap[0] = heap[size - 1]
    heapify(heap, 0, size)
    return root

def update_pos(heap, v):
    i = v.pos
    while i > 0 and heap[i].d < heap[parent(i)].d:
        heap[i].pos = parent(i)
        heap[parent(i)].pos = i
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def relax(dist, heap, u, v):
    if v.d > u.d + dist:
        v.d = u.d + dist
        update_pos(heap, v) #aktualizacja kolejki priorytetowej

def shortest_path(G, source):
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
    v.d = 0
    update_pos(q, v)
    while size:
        u = get_min(q, size)
        size -= 1
        for neighbor in u.neighbors:
            v = neighbor[0]
            relax(neighbor[1], q, u, v)
    for v in vertices:
        print(v.idx, v.d)

G1 = [
    [0, 1, 0, 11, 5, 0, 0], 
    [1, 0, 0, 5, 0, 0, 0], 
    [0, 0, 0, 0, 0, 11, 0], 
    [11, 5, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 42, 3], 
    [0, 0, 11, 0, 42, 0, 7], 
    [0, 0, 0, 0, 3, 7, 0] 
]

shortest_path(G1, 2)