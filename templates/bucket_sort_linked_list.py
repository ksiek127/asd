#dziala
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(first):
    f = first
    while f is not None:
        print(f.val)
        f = f.next

def insertion_sort(first): #zakladam, ze lista ma wartownika
    p = first
    s = Node(-1) #wartownik posortowanej listy
    if p.next is None: #lista pusta, sam wartownik
        return
    p = p.next
    while p is not None:    
        sent = s
        while s.next is not None and p.val > s.next.val: #szukam miejsca, w ktore trzeba wstawic
            s = s.next
        if s.next is None: #wstawiam na koniec
            s.next = p
            p = p.next
            s.next.next = None
        else: #wstawiam w srodek
            tmp = s.next
            s.next = p
            p = p.next
            s.next.next = tmp
        s = sent
    return s

def bucket_sort(first): #zakladam, ze wartosci sa rownomiernie rozlozone na przedziale [0, 10)
    buckets = []
    for i in range(10): #tworze kubelki
        b = Node(-1) #kazdy kubelek ma wartownika
        buckets.append(b)
    
    p = first
    p = p.next
    while p is not None: #wstawiam elementy do kubelkow
        idx = (int)(p.val)
        b = buckets[idx]
        if b.next is None: #wstawiam na koniec
            b.next = p
            p = p.next
            b.next.next = None
        else: #wstawiam zaraz po wartowniku
            tmp = b.next
            b.next = p
            p = p.next
            b.next.next = tmp
    
    for bucket in buckets: #sortuje kazdy kubelek
        bucket = insertion_sort(bucket)

    p = first
    f = p
    
    for i in range(len(buckets)): #lacze posortowane kubelki
        p.next = buckets[i].next
        while p.next is not None:
            p = p.next
    
    return f

p0 = Node(-1) #wartownik
p1 = Node(3.56)
p2 = Node(7)
p3 = Node(4.223)
p4 = Node(3.32)
p5 = Node(4.21)
p0.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p0 =bucket_sort(p0)
print_list(p0)