#dziala
def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p-1) #rekurencyjne wywolanie dla lewej czesci
        quicksort(arr, p+1, right) #dla prawej

arr = [45, 856, 432, 645, 785, 345, 65, 6, 342, 8359]
quicksort(arr, 0, len(arr) - 1)
print(arr)