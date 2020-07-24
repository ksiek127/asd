class Node(): #dziala
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack():
    def __init__(self):
        self.top = Node(-1) #wartownik
        self.elements = 0

    def push(self, x):
        N = Node(x)
        N.next = self.top.next
        self.top.next = N
        self.elements += 1

    def pop(self):
        N = self.top.next
        self.top.next = N.next
        self.elements -= 1
        return N.val

    def empty(self):
        return self.elements == 0

s = Stack()
print(s.empty())
s.push(3)
s.push(7)
print(s.pop())
s.push(18)
print(s.pop())
print(s.empty())
print(s.pop())
print(s.empty())