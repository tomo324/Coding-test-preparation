n = int(input())

d_list = []

for i in range(n):
    d = int(input())
    d_list.append(d)

d_list.sort()

last_num = 101
sorted_d = []

for j in range(n):
    if d_list[j] != last_num:
        sorted_d.append(d_list[j])
        last_num = d_list[j]

print(len(sorted_d))