#dziala
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

    if l < n and heap[l] < heap[i]: #jesli lewe dziecko istnieje i jest mniejsze niz root
        min_idx = l
    if r < n and heap[r] < heap[min_idx]: #jesli prawe dziecko jest jeszcze mniejsze
        min_idx = r
    if min_idx != i: #jesli ktores dziecko jest mniejsze od roota
        heap[i], heap[min_idx] = heap[min_idx], heap[i]
        heapify_top_down(heap, n, min_idx)

def heapify_bottom_up(heap, i):
    p = parent(i)
    if p >= 0:
        if heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
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

size = 0
arr = []
size += 1
insert(arr, size, 4)
size += 1
insert(arr, size, 2)
size += 1
insert(arr, size, 1)
size += 1
insert(arr, size, 8)
size += 1
insert(arr, size, 6)
print(arr)
print(pop(arr, size))
size -= 1
print(arr)
print(pop(arr, size))
size -= 1
print(arr)
print(pop(arr, size))
size -= 1
print(arr)
print(pop(arr, size))
size -= 1
print(arr)
print(pop(arr, size))
size -= 1
print(arr)
