"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C&lang=jp
"""

def bubbleSort(a, n):
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(n - 1, i, -1):
            if a[j][1] < a[j - 1][1]:
                a[j][1], a[j - 1][1] = a[j - 1][1], a[j][1]
                flag = True
        i += 1
    print(" ".join(list(map(str, a))))




n = int(input())
a = list(map(int, input().split()))
b = a[:]
bubbleSort(a, n)
selectionSort(b, n)