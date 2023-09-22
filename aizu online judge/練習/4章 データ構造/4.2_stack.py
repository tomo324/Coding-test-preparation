"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=ja
"""

s = []

for i in input().split():
    if i == "+":
        a = s.pop()
        b = s.pop()
        s.append(a + b)
    elif i == "-":
        a = s.pop()
        b = s.pop()
        s.append(b - a)
    elif i == "*":
        a = s.pop()
        b = s.pop()
        s.append(a * b)
    else:
        s.append(int(i))

print(s.pop())