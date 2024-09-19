MAX = 10005
NIL = -1

class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL

def preParse(u):
    if u == NIL:
        return
    print(" {}".format(u), end="")
    preParse(T[u].left)
    preParse(T[u].right)

def inParse(u):
    if u == NIL:
        return
    inParse(T[u].left)
    print(" {}".format(u), end="")
    inParse(T[u].right)

def postParse(u):
    if u == NIL:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    print(" {}".format(u), end="")

T = [Node() for _ in range(MAX)]

n = int(input())

for i in range(n):
    id, l, r = map(int, input().split())
    T[id].left = l
    T[id].right = r
    if l != NIL:
        T[l].parent = id
    if r != NIL:
        T[r].parent = id

for i in range(n):
    if T[i].parent == NIL:
        root = i

print("Preorder")
preParse(root)
print()

print("Inorder")
inParse(root)
print()

print("Postorder")
postParse(root)
print()
