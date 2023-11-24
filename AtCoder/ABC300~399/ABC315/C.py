n = int(input())
bk = [[] for _ in range(n+1)]

for _ in range(n):
    f, s = map(int, input().split())
    bk[f].append(s)

res = 0
best = []

for i in range(1, n+1):
    bk[i].sort(reverse=True)
    if len(bk[i]) >= 2:
        res = max(res, bk[i][0] + bk[i][1] // 2)
    if len(bk[i]) >= 1:
        best.append(bk[i][0])

best.sort(reverse=True)

if len(best) >= 2:
    res = max(res, best[0] + best[1])

print(res)