h, w = map(int, input().split())

field = [[] for _ in range(h)]

for i in range(h):
    field[i] = input()

mh = {-1, 0, 1, 0}
mw = {0, 1, 0, 1}

