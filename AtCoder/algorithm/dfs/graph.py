import sys
sys.setrecursionlimit(10 ** 6)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(h, w):
    seen[h][w] = True
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == "#":
            continue
        if seen[nh][nw]:
            continue
        dfs(nh, nw)

H, W = map(int, input().split())

field = [input() for _ in range(H)]

seen = [[False for _ in range(W)] for _ in range(H)]

sh, sw, gh, gw = 0, 0, 0, 0
for h in range(H):
    for w in range(W):
        if field[h][w] == "s":
            sh = h
            sw = w
        if field[h][w] == "g":
            gh = h
            gw = w

dfs(sh, sw)

if seen[gh][gw]:
    print("Yes")
else:
    print("No")