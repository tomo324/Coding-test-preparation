n = int(input())

def koch(n, a, b):
    if n == 0:
        return
    s = [(2 * a[0] + b[0]) / 3, (2 * a[1] + b[1]) / 3]
    t = [(a[0] + 2 * b[0]) / 3, (a[1] + 2 * b[1]) / 3]
    u = [(t[0] - s[0]) * 0.5 - (t[1] - s[1]) * (3 ** 0.5 / 2) + s[0], (t[0] - s[0]) * (3 ** 0.5 / 2) + (t[1] - s[1]) * 0.5 + s[1]]
    koch(n - 1, a, s)
    print(*s)
    koch(n - 1, s, u)
    print(*u)
    koch(n - 1, u, t)
    print(*t)
    koch(n - 1, t, b)

a = [0, 0]
b = [100, 0]
print(*a)
koch(n, a, b)
print(*b)
