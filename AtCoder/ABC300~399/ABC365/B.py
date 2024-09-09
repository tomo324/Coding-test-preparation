N = int(input())
A = list(map(int, input().split()))

A_copy = A[:]
A_copy.sort()
print(A.index(A_copy[-2]) + 1)