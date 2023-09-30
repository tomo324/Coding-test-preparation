N, M = map(int, input().split())
S = input()
T = input()

f = False
e = False

if T[0:N] == S:
    f = True
if T[-N:] == S:
    e = True

if f and e:
    print(0)
elif f == True and e == False:
    print(1)
elif f == False and e == True:
    print(2)
else:
    print(3)