# . Proszę opisać jak najszybszy algorytm, który otrzymuje na wejściu pewien
# ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
# mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
# ciąg składa się wyłącznie z liter a i b.
# Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
# powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
# algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.

def hash(x, n):
    h = 0
    for i in range(len(x)):
        h += ord(x[i]) #suma ascii
    return h % n

def find_subsequence(str, k):
    n = len(str) * k
    hashtable = [[None, 0]] * n
    curr = "x"
    for i in range(k - 1): #dolaczam do napisu pierwsze k-1 znakow
        curr += str[i]
    for i in range(k, len(str)): #dla kazdego podciagu
        #przesuwam podciag o jedno miejsce w prawo
        curr += str[i] #dodaje litere
        curr = curr[1:] #usuwam pierwsza litere
        h = hash(curr, n)
        counter = 0
        while hashtable[h][0] is not None and hashtable[h][0] != curr and counter < n:
            h += 1
            h %= n
            counter += 1
        if counter == n: #przepelniona tablica z haszowaniem
            return -1
        if hashtable[h][0] == curr: #aktualny podciag jest juz w tablicy haszujacej
            hashtable[h][1] += 1
        else: #nie ma go
            hashtable[h][0] = curr
            hashtable[h][1] = 1
    
    max_occurrences = 0
    result = None
    for element in hashtable:
        if element[1] > max_occurrences:
            result = element[0]
            max_occurrences = element[1]

    return result

print(find_subsequence("ababaaaabb", 3))