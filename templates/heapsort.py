#dziala

def parent(i): #zwraca indeks rodzica
        return (i-1) // 2

def left_child(i): #indeks lewego dziecka
        return 2 * i + 1

def right_child(i): #indeks prawego dziecka
        return 2 * i + 2

#max heap
def heapify(heap, n, i): #funkcja heapify dla poddrzewa ktorego korzen jest pod indeksem i
    largest = i #indeks najwiekszego elementu
    l = left_child(i)
    r = right_child(i)
    if l < n and heap[l] > heap[i]: #jesli istnieje lewe dziecko i ma wieksza wartosc niz root
        largest = l
    if r < n and heap[r] > heap[largest]: #to samo dla prawego dziecka
        largest = r
    
    if largest != i: #jesli najwieksza wartosc nie jest w korzeniu, zmieniam korzen
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, n, largest)

def heap_sort(heap):
    n = len(heap)

    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)
    
    for i in range(n-1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        heapify(heap, i, 0)

arr = [452, 434, 324, 2, 44, 23, 353, 5800, 421]
heap_sort(arr)
print(arr)