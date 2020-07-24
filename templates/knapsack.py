def knapsack(W, P, max_w): #dziala
    n = len(W)
    F = [None] * n
    for i in range(n): #inicjalizuje tablice dynamiczna
        F[i] = [0] * (max_w + 1)
    for w in range(W[0], max_w + 1): #opcja wziecia pierwszej rzeczy, jesli jestem w stanie ja udzwignac
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = F[i-1][w]
            if w >= W[i]: #jesli moge udzwignac aktualnie rozpatrywany przedmiot
                F[i][w] = max(F[i][w], F[i-1][w - W[i]] + P[i]) #moge go wziac albo nie brac
    
    return F[n-1][max_w]