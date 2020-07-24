class Node(): #dziala
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue():
    def __init__(self):
        self.head = Node(-1) #wartownik
        self.tail = self.head #przy inicjowaniu poczatek i koniec ustawiam na ten sam wezel
        self.elements = 0
    
    def enqueue(self, x):
        N = Node(x)
        self.tail.next = N
        self.tail = N
        self.elements += 1

    def dequeue(self):
        if self.elements == 0:
            return
        x = self.head.next.val
        self.head.next = self.head.next.next
        self.elements -= 1
        return x

    def empty(self):
        return self.elements == 0

q = Queue()
print(q.empty())
q.enqueue(4)
q.enqueue(2)
q.enqueue(1)
q.enqueue(8)
print(q.dequeue())
print(q.empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.empty())
print(q.dequeue())
print(q.empty())