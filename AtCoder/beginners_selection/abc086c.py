class visit:
    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y

def search(visit_list, x, y, t, cnt):
    # すでに計算済みの場合は、その結果を返す
    if (x, y, t, cnt) in memo:
        return memo[(x, y, t, cnt)] 
    # 最後の目的地にいるべき時間に達しているか
    # 最終地点に到達しているかを判定するため、t >にする必要がある。
    if t > visit_list[-1].t:
        if cnt == N:
            return True
        else:
            return False
    # 目的地を通ったらcntに1足す
    if t == visit_list[cnt].t and  x == visit_list[cnt].x and y == visit_list[cnt].y:
        cnt += 1
    t += 1
    res = search(visit_list, x+1, y, t, cnt) or\
          search(visit_list, x-1, y, t, cnt) or\
          search(visit_list, x, y+1, t, cnt) or\
          search(visit_list, x, y-1, t, cnt)
    # 結果をメモに保存
    memo[(x, y, t, cnt)] = res
    return res


N = int(input())

visit_list = [None] * N 

for i in range(N):
    t, x, y = map(int, input().split())
    visit_list[i] = visit(t, x, y)

# スタート地点の座標
x, y = 0, 0

cnt = 0
t = 0

memo = {}
res = search(visit_list, x, y, t, cnt)
if res:
    print("Yes")
else:
    print("No")