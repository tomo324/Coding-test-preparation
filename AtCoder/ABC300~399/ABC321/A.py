N = input()
flag = True

for i in range(len(N) - 1):
    if N[i] <= N[i + 1]:
        print("No")
        flag = False
        break

if flag:
    print("Yes")