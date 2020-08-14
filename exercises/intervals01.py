#dziala
def find_intervals(arr): #sprawdzic, czy istnieje taki wybor przedzialow, zwraca ilosc przedzialow lub -1 jesli nie istnieje
    arr.sort(key=lambda interval: interval[0]) #sortuje po poczatkach przedzialow
    k = 0 #iterator
    end = 0
    next_end = -1
    counter = 0 #ilosc przedzialow potrzebnych do pokrycia [0, 1]
    while k < len(arr) and end != 1:
        if arr[k][0] > end: #jesli nie ma przedzialu, ktory sie zaczyna wczesniej, niz poprzedni konczy
            return -1
        while k < len(arr) and arr[k][0] <= end: #z przedzialow, ktore sie zaczynaja wczesniej, niz poprzedni konczy, szukam tego, ktory sie konczy najpozniej
            if arr[k][1] > next_end:
                next_end = arr[k][1]
            k += 1
        end = next_end
        counter += 1
    if end != 1:
        return -1
    return counter
    
arr1 = [ [0, 0.223], [0, 0.345], [0.178, 0.344], [0.344, 0.465], [0.432, 0.734], [0.531, 0.832], [0.721, 0.988], [0.766, 1], [0.970, 1] ]
arr2 = [ [0, 0.223], [0, 0.345], [0.178, 0.344], [0.344, 0.465], [0.432, 0.734], [0.531, 0.832], [0.721, 0.988] ]
arr3 = [ [0, 0.223], [0, 0.345], [0.178, 0.344], [0.432, 0.734], [0.531, 0.832], [0.721, 0.988], [0.766, 1], [0.970, 1] ]
print(find_intervals(arr1)) # 5
print(find_intervals(arr2)) # -1
print(find_intervals(arr3)) # -1