#dziala
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def fix_list(first):
    p = first
    q = p.next
    while q is not None: #szukam elementu nie na swoim miejscu
        if q.val < p.val:
            wrong = q
            p.next = q.next
            break
        p = p.next
        q = q.next
    p = first
    q = p.next
    if wrong.val < p.val: #wstawiam na poczatek
        wrong.next = p
        return wrong
    while q is not None and not p.val < wrong.val < q.val:
        p = p.next
        q = q.next
    if q is None: #wstawiam na koniec
        p.next = wrong
    else: #wstawiam pomiedzy p i q
        p.next = wrong
        wrong.next = q
    return first

def print_linked_list(first):
    f = first
    while f is not None:
        print(f.val)
        f = f.next

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
f = fix_list(p1)
print_linked_list(f)