# 5min

N = int(input())
S = input()

flag = False

for i in range(N):
    if S[i:i+3] == "ABC":
        flag = True
        print(i+1)
        break

if not flag:
    print(-1)
