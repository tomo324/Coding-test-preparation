# n = int(input())
# S = list(map(int, input().split()))
# q = int(input())
# T = list(map(int, input().split()))

# cnt = 0

# for i in range(q):
#     for j in range(n):
#         if T[i] == S[j]:
#             cnt += 1
#             break
# print(cnt)

# 上のコードでも動くが、下のコードの方が早い

def search(a, n, key):
    i = 0
    a[n] = key
    while a[i] != key:
        i += 1
    return i != n

n = int(input())
a = input().split()
a.append(None)
q = int(input())
t = input().split()

sum = 0

for key in t:
    if search(a, n, key):
        sum += 1
print(sum)