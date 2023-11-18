import numpy as np

N = int(input())
N_list = [0] * N

S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            if S[i][j] == "o":
                N_list[i] += 1
            else:
                N_list[j] += 1
        else:
            continue

result = []

# argmaxで最大のインデックスを取得して、使ったものは負の値で置き換える。インデックスを保持する
for _ in range(N):
    max_index = np.argmax(N_list)
    N_list[max_index] = -1
    result.append(max_index + 1)

print(" ".join(map(str, result)))