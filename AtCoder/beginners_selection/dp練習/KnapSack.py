n, W = map(int, input().split())
weight = [0] * 110
value = [0] * 110

# DPテーブル
dp = [[0] * 10010 for _ in range(110)]

for i in range(n):
    weight[i], value[i] = map(int, input().split())

# DP初期条件: dp[0][w] = 0
for w in range(W + 1):
    dp[0][w] = 0

# DPループ
for i in range(n):
    for w in range(W + 1):
        if w >= weight[i]:
            dp[i+1][w] = max(dp[i][w-weight[i]] + value[i], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[n][W])
