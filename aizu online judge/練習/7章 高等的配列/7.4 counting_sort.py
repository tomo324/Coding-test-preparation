"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A&lang=jp
"""

# AとBのインデックスは0から始める

n = int(input())
A = list(map(int, input().split()))

B = [None] * (n+1)
C = [0] * 10001

k = 10000

# Aの各要素の出現回数をCに記録
for j in range(n):
    C[A[j]] += 1

# Cの要素を累積和に変える
for i in range(1, k + 1):
    C[i] += C[i-1]

for j in range(n):
    B[C[A[j]]] = A[j]
    C[A[j]] -= 1

print(" ".join(map(str, B[1:])))


