N, M = map(int, input().split())
A = list(map(int, input().split()))

j = 0

for i in range(1, N+1):
    if i == A[j]:
        print(0)
        j += 1
    else:
        day = A[j] - i
        print(day)