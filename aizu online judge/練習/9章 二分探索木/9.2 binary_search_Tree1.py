class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

root = None
NIL = Node()

def insert(k):
    global root, NIL
    y = NIL
    x = root if root is not None else NIL
    z = Node(key=k, left=NIL, right=NIL, parent=NIL)

    while x != NIL:
        y = x
        if (z.key < x.key):
            x = x.left
        else:
            x = x.right
    
    z.parent = y
    if y == NIL:
        root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z

def inorder(u):
    if u == NIL:
        return
    inorder(u.left)
    print(" {}".format(u.key), end="")
    inorder(u.right)

def preorder(u):
    if u == NIL:
        return
    print(" {}".format(u.key), end="")
    preorder(u.left)
    preorder(u.right)

n = int(input())
for i in range(n):
    com = input().split()
    if com[0] == "insert":
        insert(int(com[1]))
    elif com[0] == "print":
        inorder(root)
        print()
        preorder(root)
        print()
