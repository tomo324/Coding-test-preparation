"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A&lang=jp

解答例を再現
"""


def bubbleSort(a, n):
    sw = 0
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(n - 1, i, -1):  # i + 1を含めるためにiを指定する
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j] # 交換
                flag = True
                sw += 1
        i += 1
    print(" ".join(list(map(str, a))))
    print(sw)

n = int(input())
a = list(map(int, input().split()))
bubbleSort(a, n)
