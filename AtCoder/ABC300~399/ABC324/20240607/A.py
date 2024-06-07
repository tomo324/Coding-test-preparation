N = int(input())
A = list(map(int, input().split()))

prev = A[0]

for i in range(1, N):
    if A[i] == prev:
        prev = A[i]
    else:
        print("No")
        exit()

print("Yes")