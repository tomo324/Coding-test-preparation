N, H, X = map(int, input().split())
p_list = list(map(int, input().split()))

differ = X - H
result = 0

for i in range(len(p_list)):
    if p_list[i] >= differ:
        print(i+1)
        break