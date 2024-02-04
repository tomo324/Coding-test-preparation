D = int(input())
x, y = 0, 0
num = x ** 2 + y ** 2
for d in range(D, -1, -1):
    # x ** 2 + y ** 2 == dとなるような (x, y) の組を求める
    if num == d:
        
        print(D - d)