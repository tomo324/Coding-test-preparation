"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
思い出しながら書くことはできたがバグってしまった
ループ内で使う変数を関数内で更新したらreturnで返すようにする
"""

class P:
    def __init__(self, name, time):
        self.name = name
        self.time = time


def delete(p_list, head):
    u = p_list[head]
    head = (head + 1) % len
    return u, head

def insert(p_list, tail, u):
    p_list[tail] = u
    tail = (tail + 1) % len
    return tail


len = 100005

n, q = map(int, input().split())
p_list = [P("", 0) for _ in range(len)]

for i in range(n):
    nm, t = input().split()
    t = int(t)
    p_list[i].name = nm
    p_list[i].time = t

head = 0
tail = n

elaps = 0
while head != tail:
    u, head = delete(p_list, head) # uを取得、headを更新
    min_n = min(q, u.time)
    u.time -= min_n
    elaps += min_n
    if u.time > 0:
        tail = insert(p_list, tail, u) # uをtailの位置に代入後、tailを更新
    else:
        print(u.name + " " + str(elaps))