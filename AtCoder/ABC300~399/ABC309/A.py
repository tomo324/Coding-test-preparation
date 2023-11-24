A, B = map(int, input().split())

differ = B - A

if A != 3 and B != 4 and A != 6 and B != 7 and (differ == 1 or differ == 3):
    print("Yes")
else:
    print("No")