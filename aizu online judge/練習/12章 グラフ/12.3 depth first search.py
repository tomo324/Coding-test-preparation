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
    d[u] = tt = tt + 1 # 発見時刻を記録
    for v in range(n):
        if M[u][v] == 0: # u から v に辺がない
            continue
        if color[v] == WHITE: # u から v に辺があり、隣接ノード v が未訪問
            dfs_visit(v)
    color[u] = BLACK
    f[u] = tt = tt + 1 # 完了時刻を記録

def dfs():
    for u in range(n):
        color[u] = WHITE
    global tt
    tt = 0
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u)
    for u in range(n):
        print(u + 1, d[u], f[u])

for i in range(n):
    u, k, *v = map(int, input().split())
    u -= 1 # 1-indexed -> 0-indexed
    for j in range(k):
        v[j] -= 1 # 1-indexed -> 0-indexed
        M[u][v[j]] = 1 # u から v[j] に辺があることを記録

dfs()