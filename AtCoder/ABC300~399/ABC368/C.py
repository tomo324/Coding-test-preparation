N = int(input())
H = list(map(int, input().split()))

T = 0

for h in H:
    turn = h // 5
    h -= turn * 5
    T += turn * 3
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)