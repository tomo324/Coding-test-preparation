N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

flag = True

for i in range(N):
    for j in range(M):
        A[j] -= X[i][j]

for i in range(M):
    if A[i] > 0:
        flag = False

if flag:
    print("Yes")
else:
    print("No")