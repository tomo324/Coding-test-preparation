N = int(input())
S = input()

x = 0

for i in range(N):
    if S[i:i+3] == "ABC":
        x  += i + 1
        break

if x > 0:
    print(x)
else:
    print(-1)