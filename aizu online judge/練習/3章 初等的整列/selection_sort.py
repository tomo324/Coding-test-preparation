"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B&lang=ja

解答例を再現
"""

def selectionSort(a, n):
    sw = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
        if i != minj:
            sw += 1
    print(" ".join(list(map(str, a))))
    print(sw)

n = int(input())
a = list(map(int, input().split()))
selectionSort(a, n)