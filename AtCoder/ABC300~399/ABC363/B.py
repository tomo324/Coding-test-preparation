N, T, P = map(int, input().split())
L = list(map(int, input().split()))

done = 0

for i in range(N):
    if L[i] >= T:
        done += 1

if (done == P):
    print(0)
else:
    L.sort(reverse=True)
    target = L[P-1]
    print(T - target)