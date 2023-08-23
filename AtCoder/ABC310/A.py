"""
https://atcoder.jp/contests/abc310/tasks/abc310_a
"""

num, price, discounted = map(int, input().split())
price_list = list(map(int, input().split()))

discounted_total = discounted + min(price_list)
if discounted_total < price:
    print(discounted_total)
else:
    print(price)