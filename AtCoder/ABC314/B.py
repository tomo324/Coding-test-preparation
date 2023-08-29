def is_X(p, p_num, ans_p):
    min_p = min(len(lst) for lst in p)

    for k in p_num:
        if len(select[k]) == min_p:
            ans_p.append(k+1)

    ans_p.sort()

    print(len(ans_p))
    print(" ".join(map(str, ans_p)))


N = int(input())

select = []

for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    select.append(A)

X = int(input())
p = []
p_num = []
ans_p = []

for j in range(N):
    if X in select[j]:
        p.append(select[j])
        p_num.append(j)

if p_num:
    res = is_X(p, p_num, ans_p)
else:
    print(0)