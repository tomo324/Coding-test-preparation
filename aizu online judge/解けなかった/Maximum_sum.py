INF = float('inf')

N, K = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))

s = [0] * (N + 1)
for i in range(N):
    s[i+1] = s[i] + a[i]

res = -INF
for i in range(N - K + 1):
    val = s[K + i] - s[i]
    res = max(res, val)

print(res)