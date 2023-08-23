"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i + 1, m) or solve(i + 1, m - A_list[i])
    return res

n = int(input())
A_list = list(map(int, input().split()))
q = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    if solve(0, m):
        print("yes")
    else:
        print("no")
