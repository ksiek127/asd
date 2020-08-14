class SLNode():
    def __init__(self, val, lvl):
        self.val = val
        self.level = lvl
        self.next = []

class SkipList():
    def __init__(self):
        self.first = None
        self.last = None

MAX_LEVEL = 4

def merge(A, B):
    merged = SkipList()
    merged.first = A.first #wartownik
    for i in range(MAX_LEVEL): #lacze kazdy poziom osobno
        p = A.first.next[i]
        q = B.first.next[i]
        r = merged.first
        while p is not None and q is not None:
            if p.val < q.val:
                r.next[i] = p
                p = p.next[i]
            else:
                r.next[i] = q
                q = q.next[i]
        if p is None:
            while q is not None:
                r.next[i] = q
                q = q.next[i]
        else: #q is none
            while p is not None:
                r.next[i] = p
                p = p.next[i]
    
        