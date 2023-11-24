"""
https://atcoder.jp/contests/abc311/tasks/abc311_a
"""

n = int(input())
s = input()

a_cnt = 0
b_cnt = 0
c_cnt = 0

for i, v in enumerate(s):
    if v == "A":
        a_cnt += 1
    elif v == "B":
        b_cnt += 1
    else:
        c_cnt += 1
    if a_cnt > 0 and b_cnt > 0 and c_cnt > 0:
        print(i + 1)
        break