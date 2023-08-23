"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_C&lang=jp
"""

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def koch(n, a, b):
    if n == 0:
        return 
    th = math.radians(60)
    s = Point((2*a.x+b.x)/3, (2*a.y+b.y)/3)
    t = Point((a.x+2*b.x)/3, (a.y+2*b.y)/3)
    u = Point((t.x-s.x)* math.cos(th) - (t.y-s.y)*math.sin(th)+s.x, 
            (t.x-s.x)* math.sin(th) + (t.y-s.y)* math.cos(th) + s.y)
    
    koch(n-1, a, s)
    print(s.x, s.y)
    koch(n-1, s, u)
    print(u.x, u.y)
    koch(n-1, u, t)
    print(t.x, t.y)
    koch(n-1, t, b)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())

    a = Point(0, 0)
    b = Point(100, 0)

    print(a.x, a.y)
    koch(n, a, b)
    print(b.x, b.y)
