# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A&lang=jp

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

cnt = 0
for t in T:
    if t in S:
        cnt += 1

print(cnt)

