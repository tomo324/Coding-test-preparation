N, Q = map(int, input().split())
S = input()
a = [0] * (N+1)
b = [0] * (N+1)

# ACが出現するかどうかを判定する
for i in range(N):
    if S[i:i+2] == 'AC':
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
    # A[CA]Cのように、ACが連続している場合を考慮するため、b[r] - b[l]を出力する
    print(b[r] - b[l])