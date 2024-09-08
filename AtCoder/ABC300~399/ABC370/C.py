# S = list(input())
# T = list(input())

# X = []
# now = ""
# isSkipped = False

# for i in range(len(S)):
#     if i == 0 and S[i] < T[i]:
#         isSkipped = True
#         continue
#     if S[i] == T[i]:
#         continue
#     S[i] = T[i]
#     X.append(S.copy()) # 参照渡しを防ぐためにcopy()を使う
# if isSkipped:
#     S[0] = T[0]
#     X.append(S.copy())

# print(len(X))

# if len(X) > 0:
#     for i in range(len(X)):
#         print("".join(X[i]))


S, T = input(), input()
N = len(S)

X = []
while S != T:
    best = ""
    for i in range(N):
        if S[i] != T[i]:
            ns = list(S)
            ns[i] = T[i]
            ns = "".join(ns)
            if best == "":
                best = ns
            else:
                best = min(best, ns)
    S = best
    X.append(S)

print(len(X))
for x in X:
    print("".join(x))