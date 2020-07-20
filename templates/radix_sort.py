#dziala
def counting_sort(arr, exp):
    count = [0] * 10
    n = len(arr)
    for i in range(n): #zliczanie
        count[(arr[i]//exp) %10] += 1

    for i in range(1, len(count)): #dodawanie
        count[i] += count[i-1]

    result = [0] * n

    for i in range(n-1, -1, -1): #wpisywanie liczb na swoje miejsca
        result[count[(arr[i] // exp) % 10] -1] = arr[i]
        count[(arr[i] // exp) % 10] -= 1

    for i in range(n):
        arr[i] = result[i]

def radix(arr):
    k = 1
    max_nr = max(arr)
    while max_nr // k > 0: #sortowanie wzgledem kazdej cyfry zaczynajac od najmniej znaczacej
        counting_sort(arr, k)
        k *= 10

arr = [45, 856, 432, 645, 785, 345, 65, 6, 342, 8359]
radix(arr)
print(arr)