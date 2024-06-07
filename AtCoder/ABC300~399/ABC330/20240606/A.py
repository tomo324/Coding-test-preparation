N, L = map(int, input().split())
A = list(map(int, input().split()))

success = 0

for i in range(N):
    if A[i] >= L:
        success += 1

print(success)