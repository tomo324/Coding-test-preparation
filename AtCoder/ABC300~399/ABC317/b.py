N = int(input())
A = list(map(int, input().split()))
A.sort()

min_num = min(A)
max_num = max(A)
complete_list = []

for i in range(min_num, max_num+1):
    complete_list.append(i)

for j in range(len(complete_list)):
    if A[j] != complete_list[j]:
        print(complete_list[j])
        break