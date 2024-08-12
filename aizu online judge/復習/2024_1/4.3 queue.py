"""
何も見ずに解けたが、解答例とは違うアプローチ
"""

n, q = map(int, input().split())
Q = [input().split() for i in range(n)]

elasped = 0
finished = []

while Q:
    for i in range(len(Q)):
        now = Q.pop(0)
        c = min(q, int(now[1]))
        elasped += c
        now[1] = str(int(now[1]) - c)
        if now[1] != '0':
            Q.append(now)
        else:
            finished.append(now[0] + ' ' + str(elasped))

print('\n'.join(finished))