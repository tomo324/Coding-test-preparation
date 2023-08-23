N = int(input())

t, x, y = [0], [0], [0]

for _ in range(N):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)

can = True
for i in range(N):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dist > dt:
        can = False
    if dist % 2 != dt % 2:
        can = False

if can:
    print("Yes")
else:
    print("No")