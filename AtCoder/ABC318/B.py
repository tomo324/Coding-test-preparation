N = int(input())
area = [[""] * 110 for _ in range(110)]

for _ in range(N):
    s_x, l_x, s_y, l_y = map(int, input().split())
    for y in range(s_y, l_y):
        for x in range(s_x, l_x):
            area[y][x] = "#"

counter = 0
for i in range(110):
    for j in range(110):
        if area[i][j] == "#":
            counter += 1

print(counter)