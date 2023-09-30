K = int(input())

ans = []
for bit in range(2, 1 << 10):
    x = 0
    for i in range(9, -1, -1):
        if bit & (1 << i):
            x *= 10
            x += i
    ans.append(x)

ans.sort()
print(ans[K - 1])