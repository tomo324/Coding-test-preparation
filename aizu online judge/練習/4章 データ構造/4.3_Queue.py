"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
"""

class P:
    def __init__(self, name, t):
        self.name = name
        self.t = t

n, q = map(int, input().split())

LEN = 100005

head = 0
tail = n
Q = [P('', 0) for _ in range(LEN)]
for i in range(n):
    Q[i].name, num = input().split()
    Q[i].t = int(num)

def enqueue(Q, x, tail):
    Q[tail] = x
    tail = (tail + 1) % LEN
    return tail

def dequeue(Q, head):
    x = Q[head]
    head = (head + 1) % LEN
    return x, head

elaps = 0

while head != tail:
    u, head = dequeue(Q, head)
    c = min(q, u.t)
    u.t -= c
    elaps += c
    if u.t > 0:
        tail = enqueue(Q, u, tail)
    else:
        print(u.name + " " + str(elaps))


