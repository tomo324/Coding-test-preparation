N = 100
INFTY = 1<<21 # 十分大きな値

n = int(input())
M = [[0 for i in range(n)] for j in range(n)]

d = [0 for i in range(n)] # ノードの距離

def bfs(s):
    q = []
    q.append(s)
    for i in range(n):
        d[i] = INFTY
    d[s] = 0
    while len(q) > 0:
        u = q.pop(0) # 訪問完了
        for v in range(n):
            if M[u][v] == 0: # u から v に辺がない
                continue
            if d[v] != INFTY: # ノード v が既に訪問済み
                continue
            d[v] = d[u] + 1 # u から v に辺があるかつ未訪問なので、ノードvの距離を記録
            q.append(v) # 訪問する
    for i in range(n):
        print(i+1, -1 if d[i] == INFTY else d[i])

for i in range(n):
    u, k, *v = map(int, input().split())
    u -= 1 # 1-indexed -> 0-indexed
    for j in range(k):
        v[j] -= 1 # 1-indexed -> 0-indexed
        M[u][v[j]] = 1 # u から v[j] に辺があることを記録

bfs(0) # ノード 0 から探索を開始