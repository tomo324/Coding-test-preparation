N = int(input())
A = [None] + list(map(int, input().split()))

flag = True
ans = ""

for i in range(1, N+1):
    if not flag:
        break
    temp_list = []
    temp_set = set()
    cur = A[i]
    while flag:
        if cur not in temp_set and len(temp_list) < N:
            temp_list.append(cur)
            temp_set.add(cur)
            cur = A[cur]
        else:
            break
        if cur == A[i]:
            flag = False
            ans = temp_list

print(len(ans))
print(" ".join(map(str, ans)))

"""
n = int(input())
a = [0] + [int(x) for x in input().split()]

fl = [0] * (n + 1)
s = []
v = 1  # 任意の頂点から開始

while fl[v] == 0:
    fl[v] = 1
    s.append(v)
    v = a[v]

res = []
for nx in s:
    if nx == v:
        v = -1
    if v == -1:
        res.append(nx)

print(len(res))
print(" ".join(map(str, res)))

"""