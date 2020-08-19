#dziala
def hash(s, n1): #prosta funkcja haszujaca
    h = 0
    for c in s: #dla kazdego znaku zmiennej
        h += ord(c)
    return h % n1

def set_variables(variables, clauses):
    m = len(clauses) #ilosc klauzul
    n = len(variables) #ilosc zmiennych
    size = 2 * n #rozmiar tablicy haszujacej
    hashtable = [[-1, 0]] * size
    #zliczam wystapienia kazdej zmiennej
    for clause in clauses: #dla kazdej klauzuli
        for variable in clause: #dla kazdej zmiennej w klauzuli
            h = hash(variable, size)
            while hashtable[h][0] != variable and hashtable[h][0] != -1: #szukam zmiennej w tablicy z haszowaniem
                h += 1
                h %= n
            if hashtable[h][0] == variable: #jesli znalazlem
                hashtable[h][1] += 1 #zwiekszam licznik wystapien
            if hashtable[h][0] == -1: #jesli nie znalazlem
                hashtable[h] = [variable, 1] #dodaje do tablicy
    satisfied = 0 #ilosc spelnionych klauzul
    variables_used = [] #zmienne uzyte do spelnienia klauzul
    while len(variables) > 0 and satisfied < m / 2: #dopoki zostaly jakies zmienne i nie jest spelniona wystarczajaca ilosc klauzul
        idx = 0 #indeks zmiennej, ktora wystepuje najwieksza ilosc razy
        max_occurrences = 0 #najwieksza ilosc wystapien zmiennej
        for i in range(len(variables)): #szukam maksimum
            h = hash(variables[i], size)
            while hashtable[h][0] != variables[i] and hashtable[h][0] != -1: #szukam zmiennej w tablicy z haszowaniem
                h += 1
                h %= size
            if hashtable[h][0] == variables[i] and hashtable[h][1] > max_occurrences: #aktualizuje maksimum
                max_occurrences = hashtable[h][1]
                idx = i
        for clause in clauses: #sprawdzam, w ktorych klauzulach pojawia sie najczesciej wystepujaca zmienna    
            if variables[idx] in clause: #jesli ta zmienna jest w aktualnie przetwarzanej klauzuli
                satisfied += 1 #spelniam klauzule
                for variable in clause: #zmniejszam ilosc wystapien zmiennych z tej klauzuli
                    h = hash(variable, size)
                    while hashtable[h][0] != variable: #szukam zmiennej w tablicy z haszowaniem
                        h += 1
                        h %= size
                    hashtable[h][1] -= 1
        variables_used.append(variables[idx]) #dodaje zmienna do uzytych
        #usuwam zuzyta zmienna z tablicy (oraz jej negacje)
        if idx % 2 == 1: #jesli byla niezanegowana
            del variables[idx + 1]
            del variables[idx]
        else: #jesli zanegowana
            del variables[idx]
            del variables[idx]
    if satisfied >= m / 2:
        print("uzyte zmienne: ")
        print(variables_used)
    else:
        print("nie udalo sie spelnic polowy klauzul")

variables1 = ['a', '~a', 'b', '~b', 'c', '~c', 'd', '~d']
clauses1 = [
    ['~a', 'b'],
    ['~b', 'c'],
    ['a', 'd'],
    ['~c']
]
set_variables(variables1, clauses1)