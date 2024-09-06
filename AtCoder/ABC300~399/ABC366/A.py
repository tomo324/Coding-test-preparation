N, T, A = map(int, input().split())

P = N / 2

if T >= P:
    print("Yes")
elif A >= P:
    print("Yes")
else:
    print("No")