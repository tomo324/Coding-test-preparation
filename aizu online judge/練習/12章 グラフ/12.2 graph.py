n = int(input())

M = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    u, k, *v = map(int, input().split())
    u -= 1
    for j in range(k):
        v[j] -= 1
        M[u][v[j]] = 1

for i in range(n):
    print(*M[i])