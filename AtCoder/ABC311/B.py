"""
def count(D, zipped, cnt, max_cnt):
    for i in range(D):
        if all(item == "o" for item in zipped[i]):
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    return max_cnt

N, D = map(int, input().split())

S = [[] for _ in range(N)]

for i in range(N):
    S[i] += [char for char in input()]

zipped = list(zip(*S))

max_cnt = 0
cnt = 0

if len(S) == 1:
    for item in S[0]:
        if item == "o":
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)

else:
    max_cnt = count(D, zipped, cnt, max_cnt)

print(max_cnt)
"""

N, D = map(int, input().split())
S = [input() for _ in range(N)]

ans, cnt = 0, 0
for i in range(D):
    can = all(item[i] == "o" for item in S)
    if can:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)