class ht(): #chyba ok
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

def hash(x):
    return x * 421

def enlarge(h_t):
    new_size = 2 * h_t.size
    new = ht(new_size)
    for i in range(h_t.size):
        if h_t.table[i] != -1: #jesli trafilem na liczbe
            if new.table[hash(h_t[i]) % new_size] == -1: #jesli moge wpisac liczbe na swoje miejsce
                new.table[hash(h_t[i]) % new_size] = h_t.table[i] #wpisuje
                h_t.table[i] = -1 #usuwam ta liczbe z wyjsciowej tablicy
    
    #wszystkie liczby, ktore mogly byc na swoim miejscu juz tam sa, teraz wpisuje reszte
    for i in range(h_t.size):
        if h_t.table[i] != -1:
            idx = hash(h_t.table[i] % h_t.size)
            while new.table[idx] != -1:
                idx += 1
                idx %= new_size
            new.table[idx] = h_t.table[i]