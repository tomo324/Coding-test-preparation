# 解けなかった
N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = -1

for i in range(101):
    B = A.copy()
    B.append(i)
    B.sort()
    if sum(B[1:-1]) >= X:
        ans = i
        break

print(ans)