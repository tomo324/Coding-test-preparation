"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=ja

何も見ずに解けた

"""

s = input().split()

stack = []

for v in s:
    if v == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif v == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif v == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    else:
        stack.append(int(v))
print(stack.pop())