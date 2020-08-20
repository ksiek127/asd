#dziala
def max_width(s, substrings):
    n = len(s) #dlugosc napisu
    dp = [None] * (n + 1)
    for i in range(n + 1):
        dp[i] = [0] * (n + 1)
    for i in range(n + 1):
        dp[0][i] = 1
        dp[i][0] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dp[i][k-1] == 1: #jesli moge w tym miejscu dolaczyc napis
                for sub in substrings: #rozwazam opcje dolaczenia tych napisow, ktore moglbym tu dolaczyc
                    if k + len(sub) - 1 <= n: #jesli napis sie zmiesci
                        can_join = True
                        for j in range(len(sub)):
                            if sub[j] != s[k - 1 + j]: #jesli jakas litera sie rozni
                                can_join = False
                        if can_join:
                            dp[min(len(sub), i)][k + len(sub) - 1] = 1 #zaznaczam mozliwosc dolaczenia napisu
    for i in range(n+1):
        print(dp[i])
    for i in range(n, 0, -1):
        if dp[i][n] == 1:
            return i
    return -1 #nie da sie

subs = ['ab', 'abab', 'ba', 'bab', 'b']
t = 'ababbab'
print(max_width(t, subs))