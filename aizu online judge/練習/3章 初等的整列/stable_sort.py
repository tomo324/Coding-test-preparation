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
                a[j], a[j - 1] = a[j - 1], a[j]
                flag = True
        i += 1
    print(" ".join(list(map(str, a))))

def selectionSort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    print(" ".join(list(map(str, a))))



n = int(input())
a = list(map(str, input().split()))
b = a[:]
bubbleSort(a, n)
print("Stable")
selectionSort(b, n)
if a == b:
    print("Stable")
else:
    print("Not stable")