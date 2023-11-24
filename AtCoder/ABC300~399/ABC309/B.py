N = int(input())

A_list = []
res = [[0] * N for _ in range(N)]

for _ in range(N):
    A = input().split()
    A_list += A

for i in range(1, N):
    res[0][i] = A_list[0][i - 1]
    res[i][-1] = A_list[i - 1][-1]
    res[-1][i-1] = A_list[-1][i]
    res[i-1][0] = A_list[i][0]

for j in range(1, N-1):
    for k in range(1, N - 1):
        res[j][k] = A_list[j][k]

for row in range(N):
    print("".join(res[row]))