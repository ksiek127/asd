#dziala ALE trzeba zmienic ilosc kubelkow zeby sortowanie bylo w czasie stalym
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1

def b_sort(arr): #zakladam, ze liczby rownomiernie rozlozone na przedziale [0, 10)
    buckets = []
    for i in range(10): #tworze kubelki
        buckets.append([])
    for el in arr: #wrzucam elementy do kubelkow
        idx = (int)(el)
        buckets[idx].append(el)
    
    for bucket in buckets: #sortowanie kazdego kubelka
        insertion_sort(bucket)

    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

arr1 = [5.6557, 4.21, 5.757, 5.668, 3.5, 4.534, 3.667, 8.665, 9.44, 7.65, 8.332]
b_sort(arr1)
print(arr1)