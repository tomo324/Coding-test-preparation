# xのインデックスとそのプレイヤーのforループでのインデックスが同じ＝＝まだ解いてない
# 毎回配列をリセット
# それぞれの人物のループ* 問題のループ
# プレイヤーごとの点数を計算して、プレイヤーと同じインデックスにいれる
# それ以外ならまだ解いていない問題をループの中で探索し、その問題を配列に追加
# もし最大が自分だったら答えはゼロ
# その配列から大きい順に取得し、プレイヤーの必要回答数に加算.
# 最大値を超えた時点で配列からの取得はストップ

import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

point = [0] * N


havent_solved = [[0] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            point[i] += A[j]
        else:
            havent_solved[i].append(A[j])
    point[i] += i+1

    
max_point = max(point)

for i in range(N):
    need_num = 0
    # プレイヤーの点数が最大なら0を出力
    if point[i] == max_point:
        print(need_num)
    else:
        # プレイヤーの獲得ポイントが先ほど算出した最大値を越すまでループ
        while point[i] <= max_point:
            max_index = np.argmax(havent_solved[i])
            max_not_solved = havent_solved[i].pop(max_index)
            point[i] += max_not_solved
            need_num += 1
        print(need_num)
