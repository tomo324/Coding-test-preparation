N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = []

res = 101

for i in range(101):
    B = A[:]
    B.append(i)
    B.sort()
    if sum(B[1:-1]) >= X:
        res = min(res, i)

if res <= 100:
    print(res)
else:
    print(-1)