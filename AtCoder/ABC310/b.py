"""
https://atcoder.jp/contests/abc310/tasks/abc310_b
"""

class Product:
    def __init__(self, price, func):
        self.price = price
        self.func = func

n, m = map(int, input().split())

product_list = []

for i in range(n):
    p = list(map(int, input().split()))
    p_price = p.pop(0)
    p = p[1:]
    product_list.append(Product(p_price, p))

flag = 0

for i, a in enumerate(product_list):
    for j, b in enumerate(product_list):
        if i != j and flag == 0:
            if a.price >= b.price:
                if all(element in a.func for element in b.func):
                    if a.price > b.price or set(b.func) - set(a.func):
                        print("Yes")
                        flag += 1

if flag == 0:
    print("No")