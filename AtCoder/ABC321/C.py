K = int(input())

nums = []

for i in range(2, 1 << 10):
    x = 0
    for j in range(9, -1, -1):
        if (i & (1 << j)):
            x *= 10
            x += j
    nums.append(x)

nums.sort()
print(nums[K-1])