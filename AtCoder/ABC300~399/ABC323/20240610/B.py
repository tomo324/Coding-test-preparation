N = int(input())
S = [input() for _ in range(N)]

win_num = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            win_num[i] += 1

rank = [i+1 for i, _ in sorted(enumerate(win_num), key=lambda x: x[1], reverse=True)]

print(*rank)