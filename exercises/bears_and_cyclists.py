class Cyclist():
    def __init__(self, s_id):
        self.s_id = s_id #swoj identyfikator
        self.n_id = -1 #identyfikator rowerzysty przed nim
        self.p_id = -1 #identyfikator rowerzysty za nim
        self.visited = False

def hash(x, n):
    return x % n

def smallest_group(C):
    n = len(C) #C - tablica rowerzystow
    hashtable = [-1] * 2 * n
    for c in C: #haszuje rowerzystow
        h = hash(c.s_id, len(hashtable))
        counter = 0
        while counter < len(hashtable) and hashtable[h] != -1:
            h += 1
            h %= len(hashtable)
            counter += 1
        if counter == len(hashtable):
            print("tablica z haszowaniem przepelniona")
            return -1
        hashtable[h] = c
    for c in C: #inicjalizuje id poprzednika
        if c.n_id != -1: #jesli c ma nastepnika
            next_idx = hash(c.n_id, len(hashtable))
            while hashtable[next_idx].s_id != c.n_id: #szukam nastepnika w tablicy
                next_idx += 1
                next_idx %= len(hashtable)
            hashtable[next_idx].p_id = c.s_id
    smallest = n #rozmiar najmniejszej grupy, inicjalizuje z najwieksza mozliwa wartoscia, pozniej aktualizuje
    for c in C:
        if not c.visited:
            c.visited = True
            curr = 1 #rozmiar aktualnie rozpatrywanej grupy
            c1 = c
            while c1.n_id != -1: #licze rowerzystow z przodu
                h = hash(c1, len(hashtable)) #szukam nastepnika w tablicy
                while hashtable[h].s_id != c1.n_id:
                    h += 1
                    h %= len(hashtable)
                curr += 1
                c1 = hashtable[h]
                c1.visited = True
            while c1.p_id != -1: #licze rowerzystow z tylu
                h = hash(c1, len(hashtable)) #szukam poprzednika w tablicy
                while hashtable[h].s_id != c1.p_id:
                    h += 1
                    h %= len(hashtable)
                curr += 1
                c1 = hashtable[h]
                c1.visited = True
            if curr < smallest:
                smallest = curr

