S = input()

flag = True

for i in range(1, len(S)):
    if (i+1) % 2 == 0:
        if S[i] != "0":
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")