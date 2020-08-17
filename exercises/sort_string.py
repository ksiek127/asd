#dziala
def counting_sort(arr, pos):
    count = [0] * 27
    n = len(arr)
    for i in range(n): #zliczanie
        if len(arr[i]) > pos:
            count[ord(arr[i][pos]) - 96] += 1
        else:
            count[0] += 1

    for i in range(1, len(count)): #dodawanie
        count[i] += count[i-1]

    result = [0] * n

    for i in range(n-1, -1, -1): #wpisywanie liczb na swoje miejsca
        if len(arr[i]) > pos:
            idx = ord(arr[i][pos]) - 96
        else:
            idx = 0
        result[count[idx] -1] = arr[i]
        count[idx] -= 1

    for i in range(n):
        arr[i] = result[i]

def sort_strings(arr):
    max_len = 0
    for s in arr: #szukam najwiekszej dlugosci napisu
        if len(s) > max_len:
            max_len = len(s)
    max_len -= 1
    while max_len >= 0: #sortowanie wzgledem kazdej litery zaczynajac od najmniej znaczacej
        counting_sort(arr, max_len)
        max_len -= 1

arr = ["random", "nonsense", "string", "to", "sort", "chupa", "chups", "armadillo", "xd", "xdd", "today"]
sort_strings(arr)
print(arr)