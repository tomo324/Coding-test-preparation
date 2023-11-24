N, Q = map(int, input().split())
S = input()

a = [0] * (N+1)
b = [0] * (N+1)

# 文字が連続しているかどうかを判定する
for i in range(N-1):   # N-1まででないと、S[i+1]が存在しない
    if S[i] == S[i+1]:
        a[i] = 1

# 累積和を求め、配列に格納
for i in range(N):
    b[i+1] = b[i] + a[i]

# クエリを処理する
for i in range(Q):
    l, r = map(int, input().split())
    # l, rは1-indexedなので、0-indexedに変換する
    l -= 1
    r -= 1
    # a[ss]saaのように、文字が連続している場合を考慮するため、b[r+1] - b[l]ではなく、b[r] - b[l]を出力する
    print(b[r] - b[l])


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
