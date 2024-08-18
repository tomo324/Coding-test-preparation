# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

cnt = 0

for t in T:
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if S[mid] == t:
            cnt += 1
            break
        elif t < S[mid]:
            right = mid
        else:
            left = mid + 1

print(cnt)