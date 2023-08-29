M = int(input())

D = list(map(int, input().split()))

total = sum(D)
mid = (total+1) // 2

check_m = 0
M_i = 0
for i, d in enumerate(D):
    if d + check_m < mid:
        check_m += d
    else:
        M_i += i
        break

a = M_i + 1
b = mid - check_m

print(str(a) + " " + str(b))