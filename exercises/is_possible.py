#dziala
def hash(c, n):
    return ord(c) % n

def hash_letter(letter, size, hashtable):
    h = hash(letter, size)
    while hashtable[h][0] != letter and hashtable[h][0] != -1: #szukam litery w tablicy haszujacej
        h += 1
        h %= size
    if hashtable[h][0] == letter: #znalazlem litere
        hashtable[h][1] += 1 #zwiekszam licznik wystapien
    elif hashtable[h][0] == -1: #nie znalazlem
        hashtable[h] = [letter, 1] #wstawiam litere do tablicy

def possible(u, v, w): #czy z liter u i v da sie zrobic w
    if len(w) > len(u) + len(v):
        return False #przypadek gdy slowo w ma wiecej liter niz u i v razem
    size = 2 * (len(u) + len(v)) #tablica haszujaca nie ma szans sie przepelnic
    hashtable = [[-1, 0]] * size
    for letter in u: #dodaje do slownika kazda litere slowa u lub zwiekszam ilosc jej wystapien, jesli juz tam jest
        hash_letter(letter, size, hashtable)    
    for letter in v: #analogicznie dla v
        hash_letter(letter, size, hashtable)
    for letter in w: #dla kazdej litery slowa w, zmniejszam ilosc jej wystapien w tablicy haszujacej, jesli danej litery nie ma lub ilosc wystapien spadnie ponizej zera, nie da sie utworzyc slowa w z liter slow u i v
        h = hash(letter, size)
        while hashtable[h][0] != letter and hashtable[h][0] != -1: #szukam litery w tablicy haszujacej
            h += 1
            h %= size
        if hashtable[h][0] == letter: #znalazlem litere
            if hashtable[h][1] == 0: #wykorzystalem juz ta litere maksymalna ilosc razy
                return False
            hashtable[h][1] -= 1 #zmniejszam licznik wystapien
        elif hashtable[h][0] == -1: #nie znalazlem
            return False
    return True

u = "iksde"
v = "asdfg"
w = "dag"
print(possible(u, v, w))