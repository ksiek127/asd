class Node(): #dziala
    def __init__(self, idx):
        self.shop = False #true - sklep, false - dom
        self.distances = [] #tablica odleglosci do innych wierzcholkow
        self.edges = [] #numery wierzcholkow opisanych w distances
        self.d = float('inf') #odleglosc do najblizszego sklepu
        self.pos = idx
        self.idx = idx

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

def distance(village): #village - tablica wierzcholkow
    n = len(village) #ilosc budynkow
    fake_shop = Node(n) #wierzcholek, ktory lacze z kazdym sklepem krawedzia o wadze 0 i z niego licze najkrotsze sciezki do kazdego domu
    q = [] #kolejka priorytetowa
    fake_shop.d = 0
    fake_shop.shop = True
    village.append(fake_shop)
    for i in range(n + 1): #sprawdzam kazdy budynek
        q.append(village[i]) #dodaje do kolejki
        if village[i].shop: #jesli to jest sklep
            fake_shop.distances.append(0) #lacze go z fake_shop
            fake_shop.edges.append(i)
            village[i].distances.append(0)
            village[i].edges.append(n)
    size = len(q) #rozmiar kolejki
    while size: #dopoki kolejka nie jest pusta
        u = get_min(q, size)
        size -= 1
        for i in range(len(u.distances)): #dla kazdego sasiada
            relax(u.distances[i], q, u, village[u.edges[i]])
    for building in village:
        if not building.shop: #jesli to jest dom
            print(building.idx, building.d) #wypisuje indeks i odleglosc do najblizszego sklepu

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2.shop = True
n5.shop = True
n0.distances = [3, 5]
n0.edges = [1, 7]
n1.distances = [3, 4]
n1.edges = [0, 2]
n2.distances = [4, 1, 4]
n2.edges = [1, 5, 6]
n3.distances = [3, 3, 1]
n3.edges = [4, 6, 7]
n4.distances = [3, 7]
n4.edges = [3, 5]
n5.distances = [1, 7, 2]
n5.edges = [2, 4, 6]
n6.distances = [4, 3, 2]
n6.edges = [2, 3, 5]
n7.distances = [5, 1]
n7.edges = [0, 3]
village1 = [n0, n1, n2, n3, n4, n5, n6, n7]
distance(village1)