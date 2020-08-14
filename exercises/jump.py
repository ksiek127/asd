# class Field():
#     def __init__(self, val, lj, sj):
#         self.value = val
#         self.long_j = lj
#         self.short_j = sj
#dziala
class Field(): #uproszczenie na potrzeby testow
    def __init__(self, val):
        self.value = val
        self.long_j = 3
        self.short_j = 1

def max_val(arr):
    n = len(arr)
    arr1 = [float('-inf')] * n #ustawiam -niesk na start, wartosci beda aktualizowane
    arr1[0] = arr[0].value
    for i in range(n): #dla kazdego pola
        if i + arr[i].short_j < n: #jesli krotki skok z tego pola miesci sie w tablicy
            arr1[i + arr[i].short_j] = max(arr1[i + arr[i].short_j], arr1[i] + arr[i + arr[i].short_j].value) #sprawdzam, czy skok z tego pola powieksza wartosc na polu, na ktore skacze
        if i + arr[i].long_j < n: #jesli dlugi sie miesci
            arr1[i + arr[i].long_j] = max(arr1[i + arr[i].long_j], arr1[i] + arr[i + arr[i].long_j].value)
    return arr1[n-1]

f1 = Field(1)
f2 = Field(3)
f3 = Field(-3)
f4 = Field(7)
f5 = Field(-4)
f6 = Field(2)
f7 = Field(1)
f8 = Field(-8)
f9 = Field(5)
a1 = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
print(max_val(a1))