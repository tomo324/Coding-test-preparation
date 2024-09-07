N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ei = 1

for ej in range(1, N+1):
    if ei >= ej:
        ei = A[ei-1][ej-1]
    else:
        ei = A[ej-1][ei-1]

print(ei)