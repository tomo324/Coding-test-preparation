N = int(input())
S = [list(input()) for _ in range(N)]
max_length = max(len(sublist) for sublist in S)

ans = [[] for _ in range(max_length)]

for i in range(len(S)-1, -1, -1):
    for j in range(max_length):
        try:
            if S[i][j]:
                ans[j].append(S[i][j])
        except IndexError:
            ans[j].append("*")
            continue

while True:
    flag = 0
    for i in range(len(ans)):
        if ans[i][-1] == "*":
            del ans[i][-1]
        else:
            flag += 1
    if flag == len(ans):
        break

for i in range(len(ans)):
    print("".join(ans[i]))