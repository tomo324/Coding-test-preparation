MAX = 100005
NIL = -1

class Node:
    def __init__(self):
        self.p
        self.l
        self.r

T = [Node() for _ in range(MAX)]

def print_result(u):
    print(f'node {u}: parent {T[u].p} : depth {D[u]} : ')