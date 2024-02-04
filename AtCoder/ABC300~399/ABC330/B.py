N, L, R = map(int, input().split())
A = list(map(int, input().split()))
# 1-indexedにする
A = [0] + A

ans = []

for i in range(1, N+1):
    val = float('inf')
    if A[i] < L:
        min_val = abs(L - A[i])
    elif A[i] > R:
        min_val = abs(R - A[i])
    else:
        min_val = 0
    if A[i] <= L:
        res = A[i] + min_val
    else:
        res = A[i] - min_val
    ans.append(res)

print(*ans)


"""
    for x in range(L, R+1):
        if abs(x - A[i]) <= min_val:
            ans.append(x)
            break
"""

