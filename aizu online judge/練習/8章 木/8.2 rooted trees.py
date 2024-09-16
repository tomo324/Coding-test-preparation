MAX = 100005
NIL = -1

class Node:
    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL

T = [Node() for _ in range(MAX)]
D = [0] * MAX

def print_result(u):
    print(f'node {u}: parent {T[u].p} : depth {D[u]} : ', end='')

    if (T[u].p == NIL):
        print('root, ', end='')
    elif (T[u].l == NIL):
        print('leaf, ', end='')
    else:
        print('internal node, ',  end='')
    print('[', end='')

    i = 0
    c = T[u].l
    while c != NIL:
        if i:
            print(', ', end='')
        print(c, end='')
        c = T[c].r
        i += 1
    print(']')

def rec(u, p):
    D[u] = p
    if (T[u].r != NIL):
        rec(T[u].r, p)
    if (T[u].l != NIL):
        rec(T[u].l, p + 1)

n = int(input())
for i in range(n):
    T[i].p = NIL
    T[i].l = NIL
    T[i].r = NIL

for i in range(n):
    inputs = list(map(int, input().split()))
    v = inputs[0]
    d = inputs[1]
    children = inputs[2:]
    for j, c in enumerate(children):
        if j == 0:
            T[v].l = c
        else:
            T[l].r = c
        l = c
        T[c].p = v

for i in range(n):
    if T[i].p == NIL:
        r = i
        break
rec(r, 0)
for i in range(n):
    print_result(i)