from sympy import isprime

Q = int(input())
S = [0] * (10 ** 5 + 1)

# 1から10^5までの整数が2017-like-numberかどうかを判定する
for i in range(10 ** 5):
    if isprime(i) and isprime((i + 1) // 2):
        # 累積和を配列にメモ
        S[i + 1] = S[i] + 1
    else:
        S[i + 1] = S[i]

# クエリを処理する
for _ in range(Q):
    l, r = map(int, input().split())
    # lからrまでの区間の和を取り出して出力する
    # 1からl-1までの区間の和を引くことで、lからrまでの区間の和を取り出す
    print(S[r+1] - S[l])

