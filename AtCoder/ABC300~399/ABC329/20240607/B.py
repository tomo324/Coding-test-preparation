N = int(input())
A = list(map(int, input().split()))
max_num = max(A)

A_checked = [i for i in A if i != max_num]

print(max(A_checked))