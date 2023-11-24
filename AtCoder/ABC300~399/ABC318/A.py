N, M, P = map(int, input().split())

can_days = M
days = 0
for i in range(1, N + 1):
    if i == can_days:
        days += 1
        can_days += P

print(days)