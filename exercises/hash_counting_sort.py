from math import log2
#dziala
def hash(x, n): #funkcja haszujaca
    return x % n

def increment_counter(hashtable, x, n): #aktualizuje licznik danego elementu lub go dodaje do tablicy haszujacej jesli go w niej nie ma
    h = hash(x, n)
    while hashtable[h][0] != -1: #szukam elementu w tablicy haszujacej
        if hashtable[h][0] == x: #jesli znalazlem
            hashtable[h][1] += 1 #aktualizuje licznik
            return
        h += 1
        h %= n
    if hashtable[h][0] == -1: #jesli nie znalazlem
        hashtable[h] = [x, 1] #wpisuje do tablicy

def hash_sort(arr):
    n = len(arr)
    count_len = 2 * (int)(log2(n)) #rozmiar tablicy zliczajacej wystapienia wartosci
    count = [[-1, 0]] * count_len #tablica zliczajaca rozne wartosci
    for i in range(n):
        increment_counter(count, arr[i], count_len)
    k = 0
    while k < len(count): #usuwam puste pole
        if count[k][0] == -1:
            del count[k]
        else:
            k += 1
    count.sort(key=lambda element: element[0]) #sortuje tablice z roznymi wartosciami
    k = 0
    for i in range(len(count)): #wpisuje wartosci do wyjsciowej tablicy rosnaco
        while count[i][1] > 0:
            arr[k] = count[i][0]
            k += 1
            count[i][1] -= 1

arr1 = [349,12,12,283,349,283,283,12]
hash_sort(arr1)
print(arr1)