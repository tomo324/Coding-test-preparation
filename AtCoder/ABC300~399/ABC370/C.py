S = list(input())
T = list(input())

X = [str(len(S))]
now = ""
isSkipped = False

for i in range(len(S)):
    if i == 0 and S[i] < T[i]:
        isSkipped = True
        continue
    if S[i] == T[i]:
        continue
    S[i] = T[i]
    X.append(S)
    print(X)

if isSkipped:
    S[0] = T[0]
    X.append(S)
    print(X)