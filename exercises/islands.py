from zad1testy import runtests

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

def islands(G, source, destiny):
    n = len(G)
    vertices = []
    q = []
    adj_list = [[] for x in range(3 * n)] #tworze liste sasiedztwa
    for i in range(n): #uzupelniam ta liste
        for j in range(n):
            if G[i][j] == 1:
                adj_list[i + n].append(j)
                adj_list[i + 2 * n].append(j)
            elif G[i][j] == 5:
                adj_list[i].append(j + n)
                adj_list[i + 2 * n].append(j + n)
            elif G[i][j] == 8:
                adj_list[i].append(j + 2 * n)
                adj_list[i + n].append(j + 2 * n)
    for i in range(n): #poprawiam dane dla zrodla, bo z niego moge isc do kazdego sasiada
        if G[source][i] == 1:
            adj_list[source].append(i)
    v_nr = 3 * n #liczba wierzcholkow
    for i in range(v_nr): #wczytuje wierzcholki
        v = Node(i)
        q.append(v)
        v.pos = i
        vertices.append(v)
    for i in range(v_nr): #wczytuje sasiadow
        for neigbor_idx in adj_list[i]:
            if neigbor_idx // n == 0:
                edge_val = 1
            elif neigbor_idx // n == 1:
                edge_val = 5
            elif neigbor_idx // n == 2:
                edge_val = 8
            vertices[i].neighbors.append((vertices[neigbor_idx], edge_val))
    v = vertices[source]
    v.d = 0
    vertices[source + n].d = 0
    vertices[source + 2 * n].d = 0
    update_pos(q, v)
    update_pos(q, vertices[source + n])
    update_pos(q, vertices[source + 2 * n])
    size = v_nr
    while size:
        u = get_min(q, size)
        size -= 1
        for neighbor in u.neighbors:
            v = neighbor[0]
            relax(neighbor[1], q, u, v)
    return min(vertices[destiny].d, vertices[destiny + n].d, vertices[destiny + 2 * n].d)

runtests(islands)