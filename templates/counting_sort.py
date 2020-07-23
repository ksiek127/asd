#dziala
def c_sort(arr, x): #liczby od 0 do x
    count = [0] * (x + 1)
    n = len(arr)
    for i in range(n): #zliczam
        count[arr[i]] += 1
    for i in range(1, len(count)): #aktualizuje licznik
        count[i] += count[i-1]
    result = [0] * n
    for i in range(n-1, -1, -1):
        result[count[arr[i]] - 1] = arr[i] #wpisuje liczby w poprawnej kolejnosci do tablicy wynikowej
        count[arr[i]] -= 1

    for i in range(n):
        arr[i] = result[i]

arr = [4, 7, 6, 5, 3, 4, 5, 2, 5, 6, 5, 2, 4, 8, 6, 4, 5]
c_sort(arr, max(arr))
print(arr)