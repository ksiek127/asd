from queue import PriorityQueue
#dziala
def relax(d, uv_dist, u, v):
    d[v] = d[u] + uv_dist

def shortest_path(G, source, destiny): #lista sasiedztwa
    n = len(G)
    for i in range(n):
        G[i].sort(key = lambda x: x[1]) #sortuje sasiadow rosnaco wzgledem krawedzi od v do sasiada
    q = PriorityQueue() #do kolejki dodaje trojki [dlugosc_sciezki, indeks_wierzcholka, koszt_krawedzi_ktora_tu_przyszedlem]
    q.put([0, source, float('inf')]) #przyjmuje, ze do wierzcholka startowego dostalem sie krawedzia o nieskonczonej dlugosci, zeby moc z niego isc wszedzie
    d = [float('inf')] * n
    d[source] = 0
    while not q.empty():
        v = q.get()
        neighbors = G[v[1]]
        for i in range(len(neighbors)): #dodaje do kolejki sasiadow w kolejnosci rosnacych krawedzi, ktorymi sie do nich dostalem        
            if neighbors[i][1] < v[2]: #jesli moge isc do sasiada
                relax(d, neighbors[i][1], v[1], neighbors[i][0])
                q.put([v[0] + neighbors[i][1], neighbors[i][0], neighbors[i][1]]) #dodaje do kolejki
    return d[destiny]

# graph1 = [
# [0, 7, 0, 4, 0, 0, 0], 
# [7, 0, 6, 0, 0, 0, 0], 
# [0, 6, 0, 0, 0, 5, 0], 
# [4, 0, 0, 0, 2, 0, 0], 
# [0, 0, 0, 2, 0, 1, 0], 
# [0, 0, 5, 0, 1, 0, 3], 
# [0, 0, 0, 0, 0, 3, 0]
# ]

adj_list = [
    [[1, 7], [3, 4]],
     [[2, 6]],
      [[5, 5]],
       [[4, 2]],
        [[5, 1]],
         [[6, 3]],
         []
]

print(shortest_path(adj_list, 0, 6)) #21