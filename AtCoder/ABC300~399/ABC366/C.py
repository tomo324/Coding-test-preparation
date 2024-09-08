Q = int(input())
lst = [0] * 1000001
cnt = 0

for _ in range(Q):
    o, *x = map(int, input().split())
    if o == 3:
        print(cnt)
    elif o == 1:
        lst[x[0]] += 1
        if lst[x[0]] == 1:
            cnt += 1
    else:
        lst[x[0]] -= 1
        if lst[x[0]] == 0:
            cnt -= 1