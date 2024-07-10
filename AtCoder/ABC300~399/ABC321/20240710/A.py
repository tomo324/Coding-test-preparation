N = input()
flag = True

for i in range(len(N)-1):
    if N[i] <= N[i+1]:
        flag = False
        print("No")
        break

if flag:
    print("Yes")