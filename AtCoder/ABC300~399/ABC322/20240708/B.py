# 3min

N, M = map(int, input().split())
S = input()
T = input()

start = False
end = False

if T[0:len(S)] == S:
    start = True
if T[len(T)-len(S):] == S:
    end = True

if start and end:
    print(0)
elif start:
    print(1)
elif end:
    print(2)
else:
    print(3)