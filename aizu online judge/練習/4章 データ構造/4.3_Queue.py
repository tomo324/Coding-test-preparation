"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
"""

class P:
    def __init__(self, name, t):
        self.name = name
        self.t = t

LEN = 100005
Q = [P('', 0) for i in range(LEN)]

n, q = map(int, input().split())
head = 0
tail = n

for i in range(n):
    Q[i].name, num = input().split()
    Q[i].t = int(num)

def enqueue(Q, x, tail):
    Q[tail] = x
    tail = (tail+1) % LEN
    return tail

def dequeue(Q, head):
    x = Q[head]
    head = (head+1) % LEN
    return x, head

elapsed = 0

while head != tail:
    u, head = dequeue(Q, head)
    c = min(q, u.t)
    u.t -= c
    elapsed += c
    if u.t > 0:
        tail = enqueue(Q, u, tail)
    else:
        print(u.name + " " + str(elapsed))
