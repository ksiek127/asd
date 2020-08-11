#dziala
def partition(arr, idx_arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            idx_arr[i], idx_arr[j] = idx_arr[j], idx_arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    idx_arr[i+1], idx_arr[right] = idx_arr[right], idx_arr[i+1]
    return i + 1

def quicksort(arr, idx_arr, left, right):
    if left < right:
        p = partition(arr, idx_arr, left, right)
        quicksort(arr, idx_arr, left, p-1) #rekurencyjne wywolanie dla lewej czesci
        quicksort(arr, idx_arr, p+1, right) #dla prawej

def sumsort(A, B):
    n = len(A)
    sum_arr = [0] * n #tablica sum wierszy
    idx_arr = [0] * n
    for i in range(n):
        idx_arr[i] = i
    for i in range(n):
        for j in range(n):
            sum_arr[i] += A[i][j]
    quicksort(sum_arr, idx_arr, 0, n-1)
    for i in range(n):
        for j in range(n):
            B[i][j] = A[idx_arr[i]][j]

A = [
    [4, 2, 1, 7],
    [1, 3, 7, 7],
    [5, 8, 3, 6],
    [7, 1, 6, 3]
]
B = [0] * len(A)
for i in range(len(A)):
    B[i] = [0] * len(A)
sumsort(A, B)
for i in range(len(B)):
    print(B[i])