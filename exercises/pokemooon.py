class Node(): #dziala
    def __init__(self):
        self.idx = None
        self.preys = []
        self.visited = False

class HuntingList():
    def __init__(self, predator, prey):
        self.next = None
        self.predator = predator
        self.prey = prey

def dfs_visit(k, vertices):
    v = vertices[k]
    v.visited = True
    for p in v.preys:
        if not p.visited:
            dfs_visit(p.idx, vertices)
    print(v.idx)

def release_them_all(h_list, n):
    vertices = []

    for i in range(n): #init vertices
        v = Node()
        v.idx = i
        vertices.append(v)

    while h_list is not None: #init edges
        pred_idx = h_list.predator
        prey_idx = h_list.prey
        vertices[pred_idx].preys.append(vertices[prey_idx])
        h_list = h_list.next
    
    for v in vertices: #sprawdzam, czy w ogole da sie je wypuscic
        if len(v.preys) == 1:
            print("nie da sie")
            return
    #da sie, kolejnosc ponizej:
    k = 0
    while k < n:
        if not vertices[k].visited:
            dfs_visit(k, vertices)
        k += 1

p0 = hunting_list(0, 4)
p1 = hunting_list(2, 1)
p2 = hunting_list(5, 3)
p3 = hunting_list(0, 2)
p4 = hunting_list(2, 5)
p5 = hunting_list(4, 2)
p6 = hunting_list(5, 1)
p7 = hunting_list(4, 5)
p8 = hunting_list(2, 3)
p0.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8

release_them_all(p0, 6)