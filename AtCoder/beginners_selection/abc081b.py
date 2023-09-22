n = int(input())

a = list(map(int, input().split()))

count = 0

flag = 0
for i in range(n):
    if a[i] % 2 == 1:
        flag += 1
        break

def divide(a, count):
    flag = 0
    for i in range(n):
        a[i] = a[i] / 2
        if a[i] % 2 == 1:
            flag += 1
            break
    count += 1
    if flag == 0:
        count = divide(a, count)
    return count

if flag == 0:
    count = divide(a, count)
    print(count)
else:
    print(0)