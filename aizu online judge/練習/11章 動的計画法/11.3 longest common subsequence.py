# TLEになる

N = 1000

def lcs(X, Y):
    c = [[0 for j in range(N+1)] for i in range(N+1)]
    m = len(X)
    n = len(Y)
    maxl = 0
    X = ' ' + X
    Y = ' ' + Y

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
            maxl = max(maxl, c[i][j])
    return maxl

n = int(input())
for i in range(n):
    X = input()
    Y = input()
    print(lcs(X, Y))