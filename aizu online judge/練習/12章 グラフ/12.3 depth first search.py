# 再帰を使った深さ優先探索

N = 100

WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
M = [[0 for i in range(n)] for j in range(n)]

color = [0 for i in range(N)]
d = [0 for i in range(N)]
f = [0 for i in range(N)]
tt = 0

def dfs_visit(u):
    global tt
    color[u] = GRAY
    d[u] = tt = tt + 1
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v)
    color[u] = BLACK
    f[u] = tt = tt + 1

def dfs():
    for u in range(n):
        color[u] = WHITE
    tt = 0
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u)
    for u in range(n):
        print(u + 1, d[u], f[u])

for i in range(n):
    u, k, *v = map(int, input().split())
    u -= 1
    for j in range(k):
        v[j] -= 1
        M[u][v[j]] = 1

dfs()