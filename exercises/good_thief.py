#dziala
def thief(A):
    curr = A[0]
    prev = 0
    n = len(A)
    for i in range(1, n):
        if prev + A[i] > curr: #jesli biore przedmiot o indeksie i
            tmp = curr
            curr = prev + A[i]
            prev = tmp
        else:
            prev = curr #bedzie mozna wziac kolejny element
    return curr

arr = [5, 17, 8, 1, 11, 3]
print(thief(arr))