# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp

d = set()
n = int(input())
for _ in range(n):
    command, s = input().split()
    if command == 'insert':
        d.add(s)
    else:
        print('yes' if s in d else 'no')