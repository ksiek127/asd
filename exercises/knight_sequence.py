#dziala
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False

def in_board(x, y, n): #funkcja sprawdza, czy dane pole znajduje sie wewnatrz szachownicy
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def add_neighbor(chessboard, knights, i, j, n_i, n_j, n):
    if in_board(n_i, n_j, n):
        if chessboard[i][j] != 0 and chessboard[n_i][n_j] != 0:
            knights[i][j].neighbors.append(knights[n_i][n_j])
            knights[n_i][n_j].neighbors.append(knights[i][j])

def dfs_visit(i, j, vertices):
    v = vertices[i][j]
    v.visited = True
    for neighbor in v.neighbors:
        if not neighbor.visited:
            dfs_visit(neighbor.x, neighbor.y, vertices)

def can_jump(chessboard):
    n = len(chessboard)
    knights = [None] * n
    for i in range(n):
        knights[i] = [None] * n
    for i in range(n): #wczytuje konie i wpisuje do listy
        for j in range(n):
            if chessboard[i][j] != 0:
                knight = Node(i, j)
                knights[i][j] = knight
    for i in range(n): #krawedz jest jesli konie moga sie zbic
        for j in range(n):
            #8 pol, na ktore kon moze wskoczyc
            add_neighbor(chessboard, knights, i, j, i-1, j-2, n)
            add_neighbor(chessboard, knights, i, j, i-2, j-1, n)
            add_neighbor(chessboard, knights, i, j, i-2, j+1, n)
            add_neighbor(chessboard, knights, i, j, i-1, j+2, n)
            add_neighbor(chessboard, knights, i, j, i+1, j-2, n)
            add_neighbor(chessboard, knights, i, j, i+2, j-1, n)
            add_neighbor(chessboard, knights, i, j, i+2, j+1, n)
            add_neighbor(chessboard, knights, i, j, i+1, j+2, n)
    #sekwencja ruchow istnieje, jesli graf jest spojny
    x = 0
    y = 0
    while knights[x][y] is None: #szukam skoczka, od ktorego zaczne dfs
        if x == n:
            x = 0
            y += 1
        else:
            x += 1
    dfs_visit(x, y, knights)
    for i in range(n):
        for j in range(n):
            knight = knights[i][j]
            if knight is not None and not knight.visited: #jesli jakis kon nie zostal odwiedzony, to graf jest niespojny
                return False
    return True

board1 = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0]
]

board2 = [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0]
]

print(can_jump(board1)) #t
print(can_jump(board2)) #f