"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
"""

def search(key):
    left = 0
    right = n
    while left != right:
        mid = (left + right) // 2
        if s[mid] == key:
            return True
        elif key < s[mid]:
            right = mid
        else:
            left = mid + 1
    return False


n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

sum = 0
for key in t:
    if search(key):
        sum += 1
print(sum)
