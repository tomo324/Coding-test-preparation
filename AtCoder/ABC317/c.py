import sys
sys.setrecursionlimit(10 ** 6)


def dfs(city, current_len):
    global max_len
    max_len = max(max_len, current_len)
    seen[city] = True
    # 今の街から伸びる道路をたどって次の街を探す
    for obj in G[city]:
        if seen[obj[0]]:
            continue
        dfs(obj[0], current_len + obj[1])
    seen[city] = False

N, M = map(int, input().split())

G = [[] for _ in range(15)]

for i in range(M):
    A, B, C = map(int, input().split())
    # 繋がっている街、道の長さの順番で追加
    G[A].append([B, C])
    G[B].append([A, C])

max_len = 0

# すべての辺からスタートして試す
for start in range(1, N+1):
    # seenを初期化
    seen = [False for _ in range(15)]
    if G[start]:
        # 各スタート地点ごとに行ける最長の道を記録
        dfs(start, 0)

print(max_len)