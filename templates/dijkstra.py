class Node():
    def __init__(self, idx):
        self.idx = None
        self.neighbors = []
        self.d = float('inf')

def parent(i): #zwraca indeks rodzica
        return (i-1) // 2

def left_child(i): #indeks lewego dziecka
        return 2 * i + 1

def right_child(i): #indeks prawego dziecka
        return 2 * i + 2

def heapify_top_down(heap, n, i):
    min_idx = i
    l = left_child(i)
    r = right_child(i)

    if l < n and heap[l][1] < heap[i][1]: #jesli lewe dziecko istnieje i jest mniejsze niz root
        min_idx = l
    if r < n and heap[r][1] < heap[min_idx][1]: #jesli prawe dziecko jest jeszcze mniejsze
        min_idx = r
    if min_idx != i: #jesli ktores dziecko jest mniejsze od roota
        heap[i][1], heap[min_idx][1] = heap[min_idx][1], heap[i][1]
        heapify_top_down(heap, n, min_idx)

def heapify_bottom_up(heap, i):
    p = parent(i)
    if p >= 0:
        if heap[i][1] < heap[p][1]:
            heap[i][1], heap[p][1] = heap[p][1], heap[i][1]
            heapify_bottom_up(heap, p)

def insert(heap, n, val):
    # n += 1 #zwiekszam rozmiar kopca
    heap.append(val)
    heapify_bottom_up(heap, n-1)

def pop(heap, n): #usuwam najmniejszy element i go zwracam
    val = heap[0]
    heap[0] = heap[n-1]
    del heap[n-1] #usuwam ostatni element
    heapify_top_down(heap, n-1, 0) #naprawiam kopiec
    return val

def relax(G, u, v):
    if v.d > u.d + G[u][v]:
        v.d = u.d + G[u][v]

def shortest_path(G, source):
    vertices = []
    q = []
    n = len(G)
    for i in range(n): #init wierzcholkow
        v = Node(i)
        vertices.append(Node)

    for i in range(n): #init krawedzi
        for j in range(n):
            if G[i][j] > 0:
                vertices[i].neighbors.append[(vertices[j], G[i][j])]

    s = vertices[source]
    s.d = 0
    s.visited = True
    insert(q, len(q) + 1, s)
    while len(q) > 0:
        v = pop(q, len(q))
        for neighbor in v.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                relax(G, v, neighbor)

    for v in vertices:
        print(v.idx, v.d)

G1 = [
    [0, 1, 0, 11, 5, 0, 0], 
    [1, 0, 0, 5, 0, 0, 0], 
    [0, 0, 0, 0, 0, 11, 0], 
    [11, 5, 0, 0, 0, 0, 0], 
    [5, 0, 0, 0, 0, 42, 3], 
    [0, 0, 11, 0, 42, 0, 7], 
    [0, 0, 0, 0, 3, 7, 0], 

]

shortest_path(G1, 2)