N, M = map(int, input().split())

is_lose = [False] * N

for _ in range(M):
    win, lose = map(int, input().split())
    is_lose[lose-1] = True

winners = []
for i in range(N):
    if not is_lose[i]:
        winners.append(i+1) #1-indexedに戻す

if len(winners) == 1:
    print(winners[0])
else:
    print(-1)