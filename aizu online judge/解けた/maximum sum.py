
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))

    s = [0] * (n + 1)

    for i in range(n):
        s[i + 1] = s[i] + a[i]

    maxv = -float('inf')
    for i in range(n - k + 1):
        maxv = max(maxv, s[i+k] - s[i])

    print(maxv)
