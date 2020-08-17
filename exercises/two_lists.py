#dziala
class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class TwoLists():
    def __init__(self):
        self.even = None
        self.odd = None

def print_twolist(tl): #funkcja pomocnicza do wypisywania twolist
    e = tl.even #kopie wskaznikow
    o = tl.odd
    print("parzyste:")
    while e is not None: #wypisuje parzyste
        print(e.value)
        e = e.next
    print("nieparzyste:")
    while o is not None:
        print(o.value)
        o = o.next

def split(first):
    was_odd = False #czy byla juz pierwsza nieparzysta
    was_even = False #parzysta
    p = first #kopia wskaznika zeby nie stracic oryginalnego
    tl = TwoLists() #lista wynikowa
    while p is not None: #przechodze po kazdym elemencie wyjsciowej listy
        if p.value % 2 == 0: #jesli wartosc parzysta
            if not was_even: #jesli to jest pierwsza parzysta
                was_even = True
                tl.even = p
                p = p.next
                tl.even.next = None
                e = tl.even #kopia wskaznika 
            else: #jesli byly wczesniej jakies parzyste
                e.next = p
                e = e.next
                p = p.next
                e.next = None
        else: #jesli nieparzysta
            if not was_odd: #jesli to jest pierwsza nieparzysta
                was_odd = True
                tl.odd = p
                p = p.next
                tl.even.next = None
                o = tl.odd #kopia wskaznika
            else: #jesli byly juz nieparzyste
                o.next = p
                o = o.next
                p = p.next
                o.next = None
    return tl

p1 = Node(2)
p2 = Node(5)
p3 = Node(7)
p4 = Node(8)
p5 = Node(6)
p6 = Node(11)
p7 = Node(14)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
f = split(p1)
print_twolist(f)