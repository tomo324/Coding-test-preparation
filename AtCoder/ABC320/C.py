N = 3
M = int(input())
#S1 = list(map(str, input().split()))
#S2 = list(map(str, input().split()))
#S3 = list(map(str, input().split()))

S = [input() for _ in range(N)]

INF = 1e9

ans = INF
for i in range(N * M - 1):
    for j in range(N * M -1):
        for k in range(N * M -1):
            #if i != j and j != k and i != k and S1[i%M] == S2[j%M] == S3[k%M]:
            if i != j and j != k and i != k and S[0][i%M] == S[1][j%M] == S[2][k%M]:
                ans = min(ans, max(i, j, k))

print(ans if ans < INF else -1)