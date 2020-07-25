def s_sort(arr): #dziala
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr1 = [45, 856, 432, 645, 785, 345, 65, 6, 342, 8359]
s_sort(arr1)
print(arr1)