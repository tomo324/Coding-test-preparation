N = int(input())
A = list(map(int, input().split()))

max_num = max(A)
second_max_num = []

for i in range(N):
    if A[i] != max_num:
        second_max_num.append(A[i])

print(max(second_max_num))