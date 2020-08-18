#dziala
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(first, pivot): #rekurencyjne wywolanie dla mniejszej czesci listy
    p = first
    q = p.next
    while p.val > pivot.val: #jesli na poczatku sa elementy wieksze niz pivot
        tmp = p
        p = p.next
        tmp.next = pivot.next
        pivot.next = tmp
    first = p
    if p != pivot:
        q = p.next
        while q is not None and q != pivot: #dla kazdego elementu na lewo od pivota
            if q.val >= pivot.val: #jesli q ma wieksza wartosc niz pivot (lub rowna), przepinam go na prawo od niego
                p.next = q.next
                q.next = pivot.next
                pivot.next = q
                q = p.next
            else:
                p = p.next
                q = q.next
    last = pivot
    while last.next is not None:
        last = last.next #wskaznik na ostatni element
    if p != first:
        partition(first, p)
    if pivot != last:
        partition(pivot, last)
    return first

def print_linked_list(first):
    f = first
    while f is not None:
        print(f.val)
        f = f.next

def quickersort(head):
    pivot = head
    while pivot.next is not None:
        pivot = pivot.next #ustawiam ostatni element jako pivot
    return partition(head, pivot)

p1 = Node(7)
p2 = Node(1)
p3 = Node(7)
p4 = Node(3)
p5 = Node(6)
p6 = Node(5)
p7 = Node(3)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
q = quickersort(p1)
print_linked_list(q)