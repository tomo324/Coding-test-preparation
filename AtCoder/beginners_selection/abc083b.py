"""
N, A, B = map(int, input().split())

nums = [0] * N
total_sum = 0

i = 0
for n in range(1, N+1):
    nums[i] = str(n)
    i += 1

for i in range(N):
    digit_size = len(nums[i])
    sum_i = 0
    j = 0
    while j != digit_size:
        sum_i += int(nums[i][j])
        j += 1
    if sum_i >= A and sum_i <= B:
        total_sum += int(nums[i])

print(total_sum)


def find_sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

N, A, B = map(int, input().split())

total = 0
for i in range(1, N+1):
    sum = find_sum_of_digits(i)
    if sum >= A and sum <= B:
        total += i

print(total)
"""


def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum



N, A, B = map(int, input().split())
total = 0

for n in range(1, N+1):
    sum = sum_digit(n)
    if sum >= A and sum <= B:
        total += n

print(total)