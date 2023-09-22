# バケットを使った解法

n = int(input())

num = [0] * 110

for i in range(n):
    d = int(input())
    num[d] += 1

res = 0

for j in range(len(num)):
    if num[j] > 0:
        res += 1

print(res)