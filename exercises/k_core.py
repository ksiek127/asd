#dziala
class Node():
    def __init__(self, idx):
        self.idx = idx
        self.neighbors = [] #lista sasiadow
        self.deg = 0 #stopien wierzcholka

def remove_vertex(vertices, to_remove, v, k): #usuwam wierzcholek (i potencjalnie jego sasiadow)
    for neighbor in v.neighbors:
        neighbor.neighbors.remove(v) #usuwam v z listy sasiadow jego sasiada
        neighbor.deg -= 1 #zmniejszam stopien sasiada
    to_remove.append(v.idx)
    neighbors = v.neighbors
    vertices.remove(v) #usuwam v
    for neighbor in neighbors:
        if neighbor.deg < k:
            remove_vertex(vertices, to_remove, neighbor, k)

def remove_vertices(graph, k): #adjacency matrix
    n = len(graph) #ilosc wierzcholkow
    to_remove = [] #lista wierzcholkow do usuniecia
    vertices = []
    for i in range(n): #tworze wierzcholki
        nd = Node(i)
        vertices.append(nd)
    for i in range(n): #inicjalizuje krawedzie
        for j in range(i, len(graph[i])): #graf nieskierowany
            if graph[i][j] == 1: #jesli jest krawedz
                vertices[i].neighbors.append(vertices[j])
                vertices[j].neighbors.append(vertices[i])
                vertices[i].deg += 1
                vertices[j].deg += 1
    for v in vertices: #usuwam wierzcholki o stopniu mniejszym niz k
        if v.deg < k:
            remove_vertex(vertices, to_remove, v, k)
    if len(vertices) > 0: #jesli zostaly jakies wierzcholki
        print(to_remove)
    else:
        print("nie da sie")

graph1 = [
[0, 1, 1, 0, 1, 0, 0, 0],
[1, 0, 1, 0, 1, 0, 1, 0], 
[1, 1, 0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 1, 0, 0, 1], 
[1, 1, 0, 1, 0, 1, 1, 1], 
[0, 0, 0, 0, 1, 0, 0, 1], 
[0, 1, 1, 0, 1, 0, 0, 1], 
[0, 0, 0, 1, 1, 1, 1, 0] 
]

remove_vertices(graph1, 3) # 3, 5, 7