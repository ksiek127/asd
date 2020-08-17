#raczej dziala
class Node():
    def __init__(self):
        self.primes = [] #liczby pierwsze w postaci napisu
        self.left = None #lewe dziecko
        self.right = None #prawe dziecko

def insert(root, s): #wstawianie liczby do drzewa
    r = root #kopia wskaznika
    for i in range(len(s)):
        if s[i] == 0:
            if r.left is None: #jesli lewe dziecko nie istnieje, trzeba je stworzyc
                left = Node()
                r.left = left
            r = r.left
        else:
            if r.right is None: #analogicznie dla prawego dziecka
                right = Node()
                r.right = right
            r = r.right
    r.primes.append(s)

def contains(root, x): #czy drzewo zawiera wartosc x
    r = root
    for i in range(len(x)):
        if x[i] == 0:
            if r.left is None: #jesli lewe dziecko nie istnieje
                return False
            r = r.left
        else:
            if r.right is None:
                return False
            r = r.right
    return True

def create_set(arr):
    root = Node()
    for prime in arr:
        insert(root, prime)
    return root