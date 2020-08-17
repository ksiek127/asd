class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(first, prev_x): #rekurencyjne wywolanie dla mniejszej czesci listy
    p = first.next #aktualnie przetwarzany wskaznik
    lower = Node(-1) #elementy mniejsze od aktualnego x, lista ma wartownika
    equal = first #rowne x
    higher = Node(-1) #wieksze od x
    while p is not None and p.val < prev_x.val: #dopoki elementy sa mniejsze niz poprzedni x
        if p.val < first.val: #jesli wartosc jest mniejsza niz aktualny x
            tmp = p #wstawiam zaraz po wartowniku
            tmp.next = lower.next
            lower.next = tmp
            p = p.next
        elif p.val > first.val: #jesli jest wieksza
            tmp = p
            tmp.next = higher.next
            higher.next = tmp
            p = p.next
        else: #jesli jest rowna
            tmp = p
            tmp.next = equal.next
            equal.next = tmp
            p = p.next
    p = lower #lacze ze soba listy lower, equal i higher
    while p.next is not None:
        p = p.next
    p.next = equal #lista equal nie ma wartownika
    p = p.next
    while p.next is not None:
        p = p.next
    p.next = higher.next #omijam wartownika
    while p.next is not None:
        p = p.next
    p.next = prev_x
    partition(lower.next, equal) #rekurencyjne wywolanie dla elementow mniejszych od x
    partition(higher.next, equal) #dla wiekszych

def print_linked_list(first):
    f = first
    while f is not None:
        print(f.val)
        f = f.next

def quickersort(head):
    max_node = head
    p = head.next
    while p is not None:
        if p.val > max_node.val:
            max_node = p
        p = p.next
    partition(head, max_node)

p1 = Node(2)
p2 = Node(1)
p3 = Node(7)
p4 = Node(3)
p5 = Node(6)
p6 = Node(5)
p7 = Node(7)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
quickersort(p1)
print_linked_list(p1)