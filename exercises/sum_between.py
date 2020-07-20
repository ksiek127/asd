def partition(arr, left, right): #dziala
    x = arr[right] #pivot
    i = left
    for j in range(left, right):
        if arr[j] < x:
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
              
    arr[i], arr[right] = arr[right], arr[i] 
    return i

def kth(arr, left, right, k):
    idx = partition(arr, left, right) #indeks ostatniego elementu w posortowanej tablicy
    if idx - left == k - 1: #jezeli ostatni element w posortowanej bylby k-tym elementem
        return arr[idx] #mam wynik
    if idx - left > k - 1: #jesli bylby na prawo od k, rekurencja dla lewej czesci
        return kth(arr, left, idx - 1, k)
    else: #jesli bylby na lewo
        return kth(arr, idx + 1, right, k - idx - 1 + left)
    return -1

def sum_between(arr, f, t): #from, to
    from_val = kth(arr, 0, len(arr) - 1, f)
    to_val = kth(arr, 0, len(arr) - 1, t)
    sum = 0
    for el in arr:
        if from_val <= el <= to_val:
            sum += el
    return sum

arr = [45, 856, 432, 645, 785, 345, 65, 6, 342, 8359]
print(sum_between(arr, 2, 5))