#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.neighbors = []
        self.key = float('inf')
        self.pos = idx #pozycja w kopcu

def parent(i): #zwraca indeks rodzica
        return (i-1) // 2

def left_child(i): #indeks lewego dziecka
        return 2 * i + 1

def right_child(i): #indeks prawego dziecka
        return 2 * i + 2

def heapify(heap, idx, size):
    left = left_child(idx)
    right = right_child(idx)
    smallest = idx
    if left < size and heap[left].key < heap[idx].key:
        smallest = left
    if right < size and heap[right].key < heap[smallest].key:
        smallest = right
    if smallest != idx:
        heap[smallest].pos = idx
        heap[idx].pos = smallest
        heap[smallest], heap[idx] = heap[idx], heap[smallest]
        heapify(heap, smallest, size)

def get_min(heap, size):
    root = heap[0]
    heap[0] = heap[size - 1]
    heap[0].pos = 0
    root.pos = size - 1
    heapify(heap, 0, size - 1)
    return root    

def update_pos(heap, v):
    i = v.pos
    while i > 0 and heap[i].key < heap[parent(i)].key:
        heap[i].pos = parent(i)
        heap[parent(i)].pos = i
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def find_mst(G):
    n = len(G)
    mst = []
    heap = []
    for i in range(n): #wczytuje wierzcholki
        v = Node(i)
        heap.append(v)
    for i in range(n): #wczytuje krawedzie
        for j in range(n):
            if G[i][j] != 0:
                heap[i].neighbors.append((heap[j], G[i][j]))
    heap[0].key = 0
    size = n
    update_pos(heap, heap[0])
    while size > 0:
        u = get_min(heap, size)
        size -= 1
        for neighbor in u.neighbors:
            v = neighbor[0]
            if v.pos < size and neighbor[1] < v.key: #jesli v jest w kopcu i waga krawedzi z u do v jest mniejsza niz klucz v, aktualizuje klucz
                v.key = neighbor[1]
                mst.append((u, v))
                update_pos(heap, v)
    
    for pair in mst:
        print(pair[0].idx, pair[1].idx)

G1 = [ [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]]

find_mst(G1)