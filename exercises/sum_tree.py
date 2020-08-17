class Node(): #raczej dziala, dalo sie prosciej
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None
        self.sum_left = 0
        self.sum_right = 0

def find(x, root):
    r = root
    while r.val != x and r is not None:
        if x < r.val:
            r = r.left
        else:
            r = r.right
    if r is None:
        return -1 #nie znaleziono
    return r

def get_min(root):
    r = root
    while r.left is not None:
        r = r.left
    return r.val

def get_max(root):
    r = root
    while r.right is not None:
        r = r.right
    return r.val

def update_sums(root, x): #aktualizuje wartosci sum
    if x.left is not None: #inicjalizuje sume lewego poddrzewa x
        x.sum_left = x.left.sum_left + x.left.sum_right + x.left.val
    if x.right is not None: #analogicznie dla prawego poddrzewa
        x.sum_right = x.right.sum_left + x.right.sum_right + x.right.val
    while x != root:
        p = x.parent
        if p.left == x: #jesli x to lewe dziecko
            p.sum_left = x.sum_left + x.sum_right + x.val
        else: #jesli x to prawe dziecko
            p.sum_right = x.sum_left + x.sum_right + x.val
        x = p

def insert(root, x):
    r = root
    while r.val != x:
        if x < r.val:
            if r.left is not None:
                r = r.left
            else: #insert
                nd = Node(x)
                nd.parent = r
                r.left = nd
                update_sums(root, nd)
        elif x > r.val:
            if r.right is not None:
                r = r.right
            else: #insert
                nd = Node(x)
                nd.parent = r
                r.right = nd
                update_sums(root, nd)
        else: #jesli liczba, ktora mam wstawic juz jest w drzewie
            return

def delete(root, x):
    to_delete = find(root, x)
    if to_delete == -1: #jesli nie ma w drzewie elementu, ktory chce usunac
        return
    if to_delete.right is None and to_delete.left is None: #jesli usuwam lisc
        if to_delete.parent.left == to_delete: #jesli to jest lewy lisc
            to_delete.parent.left = None
        else:
            to_delete.parent.right = None
    elif to_delete.right is None: #jesli ma lewe poddrzewo ale nie ma prawego
        if to_delete.parent.left == to_delete: #jesli to jest lewe dziecko
            to_delete.parent.left = to_delete.left
        else:
            to_delete.parent.right = to_delete.left
    elif to_delete.right is None: #jesli ma prawe poddrzewo ale nie ma lewego
        if to_delete.parent.left == to_delete:
            to_delete.parent.left = to_delete.right
        else:
            to_delete.parent.left = to_delete.right
    else: #jesli ma oba poddrzewa
        succ = get_min(to_delete.right) #szukam nastepnika, usuwam go i wpisuje jego wartosc do to_delete
        s_val = succ.val
        delete(root, succ)
        to_delete.val = s_val
        
