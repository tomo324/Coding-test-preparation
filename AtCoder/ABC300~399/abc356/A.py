N, L, R  = map(int, input().split())
A = []

for i in range(N):
    A.append(i + 1)

while L < R:
    A[L - 1], A[R - 1] = A[R - 1], A[L - 1]
    L += 1
    R -= 1

print(" ".join(map(str, A)))