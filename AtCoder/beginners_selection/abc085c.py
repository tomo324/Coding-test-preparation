
N, Y = map(int, input().split())

res10000, res5000, res1000 = -1, -1, -1

for a in range(N+1):
    for b in range(N+1):
        c = N - a - b
        if c >= 0 and 10000*a + 5000*b + 1000*c == Y:
            res10000, res5000, res1000 = a, b, c

print("{} {} {}".format(res10000, res5000, res1000))