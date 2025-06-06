"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A&lang=ja

AtCoderの問題

"""

# keyがリストaに存在するかどうかを判定する（番兵法による線形探索）
def search(a, n, key):
    a[n] = key
    i = 0
    while a[i] != key:
        i += 1
    return i != n


n = int(input())
a = input().split()
a.append(None)
q = int(input())
t = input().split()

sum = 0
for key in t:
    if search(a, n, key):
        sum += 1
print(sum)