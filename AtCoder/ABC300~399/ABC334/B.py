A, M, L, R = map(int, input().split())

a = A % M
space = R - L

if space >= 0:
    space += a
else:
    space -= a

ans = space // M
print(ans)




"""
A, M, L, R = map(int, input().split())
tree_list = []

right_step = 0
for i in range(A, R+1):
    tree_list.append(A+right_step)
    right_step = right_step + M

left_step = 0
for i in range(A, L-1, -1):
    tree_list.append(A-left_step)
    left_step = left_step + M

set(tree_list)

ans = 0
for i in range(L, R+1):
    if i in tree_list:
        ans += 1

print(ans)
"""