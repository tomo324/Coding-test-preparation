NIL = -1
MAX = 100005

class Node():
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

def print_result(u):
    print(f'node {u}: parent = {T[u].parent}, depth = {D[u]}, ', end='')
    if T[u].parent == NIL:
        print('root, ', end='')
    elif T[u].left == NIL:
        print('leaf, ', end='')
    else:
        print('internal node, ', end='')
    print('[', end='')

    c = T[u].left
    i = 0
    while c != NIL:
        if i != 0:
            print(', ', end='')
        print(c, end='')
        c = T[c].right
        i += 1
    print(']')

def rec(u, p):
    D[u] = p
    if T[u].right != NIL:
        rec(T[u].right, p)
    if T[u].left != NIL:
        rec(T[u].left, p+1)

T = [Node() for _ in range(MAX)]
D = [0] * MAX

n = int(input())

for _ in range(n): 
    id, k, *c = map(int, input().split())
    for i in range(k):
        if i == 0:
            T[id].left = c[i]
        else:
            T[c[i-1]].right = c[i]
        T[c[i]].parent = id

for i in range(n):
    if T[i].parent == NIL:
        root = i

rec(root, 0)

for i in range(n):
    print_result(i)