NIL = -1
MAX = 10000
D = [0] * MAX
H = [0] * MAX

class Node():
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

def setDepth(u, p):
    D[u] = p
    if T[u].left != NIL:
        setDepth(T[u].left, p+1)
    if T[u].right != NIL:
        setDepth(T[u].right, p+1)

def setHeight(u):
    h1 = h2 = 0
    if T[u].left != NIL:
        h1 = setHeight(T[u].left) + 1
    if T[u].right != NIL:
        h2 = setHeight(T[u].right) + 1
    H[u] = max(h1, h2)
    return H[u]

def getSibling(u):
    if T[u].parent == NIL:
        return NIL
    if T[T[u].parent].left != u and T[T[u].parent].right != NIL:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].left != NIL:
        return T[T[u].parent].right
    return NIL

def printResult(u):
    deg = 0
    if T[u].right != NIL:
        deg += 1
    if T[u].left != NIL:
        deg += 1
    node_type = ""
    if T[u].parent == NIL:
        node_type = "root"
    elif T[u].left == NIL and T[u].right == NIL:
        node_type = "leaf"
    else:
        node_type = "internal node"
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(u, T[u].parent, getSibling(u), deg, D[u], H[u], node_type))



T = [Node() for _ in range(MAX)]

n = int(input())

# 木を構築
for i in range(n):
    id, left, right = map(int, input().split())
    T[id].left = left
    T[id].right = right
    if left != NIL:
        T[left].parent = id
    if right != NIL:
        T[right].parent = id

for i in range(n):
    if T[i].parent == NIL:
        root = i

setDepth(root, 0)
setHeight(root)

for i in range(n):
    printResult(i)