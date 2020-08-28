class Node(): #nie dziala ;c
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

def shortest_path(G, costs, capacity, source, destiny):
    n = len(G)
    vertices = []
    q = []
    size = n * (capacity + 1) #ilosc wierzcholkow
    for i in range(n): #wczytuje wierzcholki
        for j in range(capacity + 1): #robie sztuczne wierzcholki
            v = Node(i * (capacity + 1) + j)
            vertices.append(v)
            q.append(v)
            v.pos = i * (capacity + 1) + j #miejsce w kolejce priorytetowej
        for j in range(capacity):
            vertices[i * (capacity + 1) + j].neighbors.append((vertices[i * (capacity + 1) + j + 1], costs[i])) #opcja tankowania
    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                for k in range(G[i][j], capacity + 1): #moge przejsc do innego wierzcholka tylko jesli mam wystarczajaco duzo paliwa
                    vertices[i * (capacity + 1) + k].neighbors.append((vertices[j * (capacity + 1) + k - G[i][j]], 0))

    for i in range(capacity + 1):
        v = vertices[source * (capacity + 1) + i]
        v.d = i * costs[source]
        update_pos(q, v)
    while size:
        u = get_min(q, size)
        size -= 1
        for neighbor in u.neighbors:
            v = neighbor[0]
            relax(neighbor[1], q, u, v)
    min_dist = float('inf')
    for i in range(capacity + 1):
        if vertices[destiny * (capacity + 1) + i].d < min_dist:
            min_dist = vertices[destiny * (capacity + 1) + i].d
    return min_dist

graph1 = [
[0, 0, 0, 0, 0, 0, 7], 
[0, 0, 0, 3, 0, 12, 0], 
[0, 0, 0, 0, 12, 11, 0], 
[0, 3, 0, 0, 1, 0, 0], 
[0, 0, 12, 1, 0, 7, 11], 
[0, 12, 11, 0, 7, 0, 3], 
[7, 0, 0, 0, 11, 3, 0]
]

costs1 = [5, 20, 3, 3, 1, 17, 4]

print(shortest_path(graph1, costs1, 14, 5, 3))