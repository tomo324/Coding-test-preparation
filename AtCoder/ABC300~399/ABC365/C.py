# TLE

# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# for i in range(M):
#     cost = 0
#     for j in range(N):
#         c = min(i, A[j])
#         cost += c
#     if cost > M:
#         print(i - 1)
#         exit()

# print("infinite")

# AC
N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i]
if sum <= M:
    print("infinite")
    exit()

ok = 0
ng = 10 ** 9

while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    cost = 0
    for i in range(N):
        cost += min(mid, A[i])
    if cost > M:
        ng = mid
    else:
        ok = mid

print(ok)