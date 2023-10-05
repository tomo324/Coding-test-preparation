import sys
sys.setrecursionlimit(10 ** 6)


def dfs(current_length, visited, city):
    global max_length
    max_length = max(max_length, current_length)
    visited[city] = True
    for n_city in city_list[city]:
        if visited[n_city[0]]:
            continue
        dfs(current_length + n_city[1], visited, n_city[0])
    visited[city] = False

N, M = map(int, input().split())
city_list = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    city_list[A].append([B, C])
    city_list[B].append([A, C])

max_length = 0
for city_num in range(1, N + 1):
    visited = [False] * (N + 1)
    if city_list[city_num]:
        dfs(0, visited, city_num)

print(max_length)