class Node:
    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL

def print_result(u):
    print(f'node {u}: parent = {T[u].p}, depth = {D[u]}, ', end='')

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

MAX = 100005
NIL = -1

T = [Node() for _ in range(MAX)]
D = [0] * MAX

n = int(input())

for i in range(n):
    inputs = list(map(int, input().split()))
    id = inputs[0]
    k = inputs[1]
    children = inputs[2:]
    for j, c in enumerate(children):
        if j == 0:
            T[id].l = c
        else:
            T[prev].r = c
        prev = c
        T[c].p = id

for i in range(n):
    if T[i].p == NIL:
        r = i
        break

rec(r, 0)

for i in range(n):
    print_result(i)