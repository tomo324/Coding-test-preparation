import math

N = int(input())

for i in range(int(math.log(N, 2)) + 1):
    for j in range(int(math.log(N, 3)) + 1):
        if 2**i * 3**j == N:
            print("Yes")
            exit()

print("No")