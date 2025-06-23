"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A&lang=ja

解答例を再現
"""

def trace(a, n):
    print(" ".join(list(map(str, a))))

def insertion_sort(a, n):
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
            print("v: {}".format(v))
            print("a: {}".format(a))
        a[j + 1] = v
        trace(a, n)

n = int(input())
a = list(map(int, input().split()))
trace(a, n)
insertion_sort(a, n)