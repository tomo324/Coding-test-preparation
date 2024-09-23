class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

root = None
NIL = Node()

def treeMinimum(x):
    while x.left != NIL:
        x = x.left
    return x

def find(u, k):
    while u != NIL and k != u.key:
        if k < u.key:
            u = u.left
        else:
            u = u.right
    return u

def treeScuccessor(x):
    if x.right != NIL:
        return treeMinimum(x.right)
    y = x.parent
    while y != NIL and x == y.right:
        x = y
        y = y.parent
    return y

def treeDelete(z):
    global root, NIL
    y = NIL
    x = NIL
    if z.left == NIL or z.right == NIL:
        y = z
    else:
        y = treeScuccessor(z)
    if y.left != NIL:
        x = y.left
    else:
        x = y.right
    if x != NIL:
        x.parent = y.parent
    if y.parent == NIL:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.key = y.key

def insert(k):
    global root, NIL
    y = NIL # 親の候補
    x = root if root is not None else NIL # 走査用ポインタ
    z = Node(key=k, left=NIL, right=NIL, parent=NIL) # 挿入するノード

    while x != NIL:
        y = x
        if z.key < x.key:
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
    if com[0] == "find":
        t = find(root, int(com[1]))
        if t != NIL:
            print("yes")
        else:
            print("no")
    elif com[0] == "insert":
        insert(int(com[1]))
    elif com[0] == "print":
        inorder(root)
        print()
        preorder(root)
        print()
    elif com[0] == "delete":
        treeDelete(find(root, int(com[1])))