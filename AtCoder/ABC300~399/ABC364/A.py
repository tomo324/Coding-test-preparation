N = int(input())
S = [input() for _ in range(N)]

cnt = 0
isNausea = False

for i in range(N):
    if isNausea:
        print('No')
        exit()
    if S[i] == 'sweet':
        cnt +=1
        if cnt >= 2:
            isNausea = True
    else:
        cnt = 0

print('Yes')