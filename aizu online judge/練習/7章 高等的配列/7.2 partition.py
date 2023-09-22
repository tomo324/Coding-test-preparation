"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_B&lang=jp
"""

import sys
input = sys.stdin.readline

def swap(a, i, j):
    k = a[j]
    a[j] = a[i]
    a[i] = k

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i+1, r)
    return i+1

n = int(input())
A = list(map(int, input().split()))

q = partition(A, 0, n-1)

for i in range(n):
    if i:
        print(" ", end="")
    if i == q:
        print("[", end="")
    print(A[i], end="")
    if i == q:
        print("]", end="")
print()