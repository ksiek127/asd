class Node(): #cos nie dziala (albo dziala ale mega wolno)
    def __init__(self, val):
        self.val = val
        self.height = 1
        self.right = None
        self.left = None
        self.parent = None

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

def get_height(x, y, root): #zwraca wysokosc aktualnie stawianego klocka
    r = root
    while not x <= r.val <= y:
        if r.val < x:
            if r.right is not None:
                r = r.right
            else:
                 return -1
        elif r.val > y:
            if r.left is not None:
                r = r.left
            else:
                return 1
    return r.val + 1

def insert(root, x, h):
    r = root
    while r.val != x:
        if x < r.val:
            if r.left is not None:
                r = r.left
            else: #insert
                nd = Node(x)
                nd.parent = r
                r.left = nd
                nd.height = h
        elif x > r.val:
            if r.right is not None:
                r = r.right
            else: #insert
                nd = Node(x)
                nd.parent = r
                r.right = nd
                nd.height = h
        else: #jesli liczba, ktora mam wstawic juz jest w drzewie
            return

def update(nd, h, r_val): #node, height
    if nd.val < r_val: #jesli miesci sie w przedziale (ostra nierownosc, bo skrajne punkty sa poprawnie ustawione przy wstawianiu do drzewa)
        nd.height = h
        if nd.left is not None:
            update(nd.left, h, r_val)
        if nd.right is not None:
            update(nd.right, h, r_val)

def find_max(root):
    if root.left is None and root.right is None:
        return root.height
    if root.left is None:
        return max(root.height, find_max(root.right))
    if root.right is None:
        return max(root.height, find_max(root.left))
    return max(root.height, find_max(root.left), find_max(root.right))

def max_height(arr): #arr - tablica klockow w kolejnosci spadania
    n = len(arr)
    root = Node(arr[0][1]) #tworze drzewo
    nd = Node(arr[0][0])
    nd.parent = root
    root.left = nd
    for i in range(1, n):
        block_height = get_height(arr[i][0], arr[i][1], root)
        insert(root, arr[i][0], block_height)
        insert(root, arr[i][1], block_height) #wstawiam krance przedzialu do drzewa
        #aktualizuje wysokosc punktow nalezacych do przedzialu aktualnie stawianego klocka
        l_val = arr[i][0]
        r_val = arr[i][1]
        l_node = find(l_val, root)
        if l_node.right is not None: #aktualizuje prawe poddrzewo
            update(l_node.right, block_height, r_val)
        while l_node.parent is not None:
            if l_node.parent.left == l_node: #jesli l_node to lewe dziecko
                if l_node.parent.val >= r_val:
                    break
                l_node.parent.height = block_height #aktualizuje parent i jego prawe poddrzewo
                update(l_node.parent.right, block_height, r_val)
            else: #jesli to jest prawe dziecko
                if l_node.parent.parent is None:
                    break
                if l_node.parent.parent.val >= r_val:
                    break
                l_node.parent.parent.height = block_height #aktualizuje 'dziadka'
                update(l_node.parent.parent.right, block_height, r_val) #aktualizuje jego prawe poddrzewo

    r = root
    max_h = find_max(r)
    return max_h

arr1 = [(1, 3), (2, 5)]
print(max_height(arr1))