N = 100
INFTY = 1<<21

n = int(input())
M = [[0 for i in range(n)] for j in range(n)]

d = [0 for i in range(n)]

def bfs(s):
    q = []
    q.append(s)
    for i in range(n):
        d[i] = INFTY
    d[s] = 0
    while len(q) > 0:
        u = q.pop(0)
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != INFTY:
                continue
            d[v] = d[u] + 1
            q.append(v)
    for i in range(n):
        print(i + 1, -1 if d[i] == INFTY else d[i])

for i in range(n):
    u, k, *v = map(int, input().split())
    u -= 1
    for j in range(k):
        v[j] -= 1
        M[u][v[j]] = 1

bfs(0)