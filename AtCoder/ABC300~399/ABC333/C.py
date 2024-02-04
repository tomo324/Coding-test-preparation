N = int(input())

repunits = []

sum_repunits = []
for i in range(1, 14):
    for j in range(1, 14):
        for k in range(1, 14):
            sum = int("1" * i) + int("1" * j) + int("1" * k)
            if sum not in sum_repunits:
                sum_repunits.append(sum)
            else:
                continue

sum_repunits.sort()

print(sum_repunits[N-1])