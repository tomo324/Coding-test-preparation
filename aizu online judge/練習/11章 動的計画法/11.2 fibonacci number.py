n = int(input())

F = [0] * 50
F[0] = 1
F[1] = 1

for i in range(2, n+1):
    F[i] = F[i-1] + F[i-2]

print(F[n])