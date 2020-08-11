#dziala
def w_sort(A):
    even = []
    i = 0
    while i < len(A): #wykrywam parzyste
        if A[i] % 2 == 0:
            even.append(A[i])
            del A[i]
        i += 1
    even.sort() #sortuje parzyste
    result = []
    odd_idx = 0
    even_idx = 0
    while odd_idx < len(A) and even_idx < len(even): #merge dwoch tablic
        if A[odd_idx] < even[even_idx]:
            result.append(A[odd_idx])
            odd_idx += 1
        else:
            result.append(even[even_idx])
            even_idx += 1
    if odd_idx == len(A):
        while even_idx < len(even):
            result.append(even[even_idx])
            even_idx += 1
    else:
        while odd_idx < len(A):
            result.append(A[odd_idx])
            odd_idx += 1
    return result

arr = [1, 3, 42, 11, 17, 23, 29, 50, 41, 57, 421, 2, 9001]
print(w_sort(arr))