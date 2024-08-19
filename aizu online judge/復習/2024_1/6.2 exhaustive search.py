# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
# 本の通りに実装したが、TLEになる

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i + 1, m) or solve(i + 1, m - A[i])
    return res

for m in M:
    if solve(0, m):
        print("yes")
    else:
        print("no")