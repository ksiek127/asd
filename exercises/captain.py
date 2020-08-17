#dziala
def in_board(i, j, n): #czy pole [i, j] znajduje sie wewnatrz planszy n x n
    if 0 <= i < n and 0 <= j < n:
        return True
    return False

def can_sail(arr, depth):
    n = len(arr)
    can_reach = [None] * n
    for i in range(n):
        can_reach[i] = [False] * n
    if arr[0][0] < depth: #jesli poczatkowe pole jest za plytko, nie da sie plynac
        return False
    can_reach[0][0] = True
    for i in range(n): #dla kazdego pola sprawdzam, czy da sie doplynac do jego sasiadow
        for j in range(n):
            if can_reach[i][j]:
                if in_board(i-1, j, n) and arr[i-1][j] >= depth:
                    can_reach[i-1][j] = True
                if in_board(i, j-1, n) and arr[i][j-1] >= depth:
                    can_reach[i][j-1] = True
                if in_board(i+1, j, n) and arr[i+1][j] >= depth:
                    can_reach[i+1][j] = True
                if in_board(i, j+1, n) and arr[i][j+1] >= depth:
                    can_reach[i][j+1] = True
    return can_reach[n-1][n-1]

arr1 = [
    [5, 3, 8, 9, 11],
    [6, 8, 6, 7, 7],
    [7, 7, 4, 5, 1],
    [8, 1, 3, 5, 7],
    [10, 2, 2, 4, 5]
]

print(can_sail(arr1, 5))