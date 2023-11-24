N = int(input())
P = list(map(int, input().split()))

pre_p = P[0]
for i in range(1, N):
    if P[0] <= P[i]:
        P[0] += P[i] + 1 - P[0]

print(P[0] - pre_p)