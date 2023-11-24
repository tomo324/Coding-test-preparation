N, M = map(int, input().split())
S = [input() for _ in range(N)]

def check(i, j):
    # 左上の3*3の黒をチェック
    for ii in range(3):
        for jj in range(3):
            if S[i+ii][j+jj] != "#":
                return False
            
    # 右上の3*3の黒をチェック
    for ii in range(6, 9):
        for jj in range(6, 9):
            if S[i+ii][j+jj] != "#":
                return False

    # 左上の白をチェック
    for ii in range(3)



for i in range(1, N-8):
    for j in range(1, M-8):
        if check(i, j):



"""
ans = []

for i in range(N):
    for j in range(M):
        cnt = 0
        # 9*9の領域があるかチェック
        if (i+8) < N or (j+8) < M:
            continue
        opp_i, opp_j = i+8, j+8
        for a in range(4):
            for b in range(4):
                if S[i+a][j+b] == S[opp_i-a][opp_j-b]:
                    if a < 3 or b < 3 and S[i+a][j+b] == "#":
                        cnt += 1
                    if a == 3 or b == 3 and S[i+a][j+b] == ".":
                        cnt += 1
        if cnt == 16:
            pair = [i+1, j+1]
            ans.append(pair)

for lst in ans:
    print(" ".join(map(str, lst)))
"""
