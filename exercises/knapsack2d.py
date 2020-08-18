#chyba ok
def knapsack(W, H, P, max_w, max_h): #W - wagi przedmiotow, H - wysokosci, P - ceny
    n = len(W) #ilosc przedmiotow
    F = [None] * n
    for i in range(n): #inicjalizuje tablice dynamiczna
        F[i] = [0] * (max_w + 1)
        for j in range(n):
            F[i][j] = [0] * (max_h + 1)
    for w in range(W[0], max_w + 1): #opcja wziecia pierwszej rzeczy, jesli jestem w stanie ja udzwignac
        for h in range(H[0], max_h + 1):
            F[0][w][h] = P[0]
    for i in range(1, n):
        for w in range(1, max_w + 1):
            for h in range(1, max_h + 1):
                F[i][w][h] = F[i-1][w][h]
                if w >= W[i] and h >= H[i]: #jesli moge udzwignac aktualnie rozpatrywany przedmiot
                    F[i][w][h] = max(F[i][w][h], F[i-1][w - W[i]][h - H[i]] + P[i]) #moge go wziac albo nie brac
    
    return F[n-1][max_w][max_h]