N = int(input())

ans = ""

for i in range(N + 1):
    min_j = 10
    for j in range(1, 10):
        if i == 0:
            if N % j == 0:
                min_j = min(min_j, j)
        else:
            if N % j == 0 and i % (N / j) == 0:
                min_j = min(min_j, j)
    if min_j <= 9:
        ans += str(min_j)
    else:
        ans += "-"

print(ans)

"""
i = 4
j = 1, 2, 3, 4, 6

i is a multiple of N/j
N / j == 12 / (1 or 2 or 3 or 4 or 6)
j == 4
"""