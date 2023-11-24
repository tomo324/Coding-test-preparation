"""
TLEする

N, Q = map(int, input().split())
S = input()

# 1-indexedにする
S = " " + S

# memo[i] = [l, r, cnt]
memo = []

for i in range(Q):
    flag = False
    cnt = 0
    l, r = map(int, input().split())
    # メモ化している区間の中にl, rが含まれているか
    for j in range(len(memo)):
        if l <= memo[j][0] and r >= memo[j][1]:
            cnt += memo[j][2]
            flag = True
    # メモ化している区間の中にl, rが含まれている場合
    if flag:
        for k in range(l, memo[j][0]):
            if S[k] == S[k+1]:
                cnt += 1
        for k in range(memo[j][1], r):
            if S[k] == S[k+1]:
                cnt += 1
        memo.append([l, r, cnt])
        print(cnt)
        continue
    # メモ化している区間の中にl, rが含まれていない場合
    for j in range(l, r):
        if S[j] == S[j+1]:
            cnt += 1
    memo.append([l, r, cnt])
    print(cnt)
"""
