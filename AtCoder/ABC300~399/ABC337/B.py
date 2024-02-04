S = input()
flag = True

for i in range(len(S)):
    if S[i] == "A":
        if i < (len(S) - 1):
            if S[i+1] == "C":
                flag = False
                break
    elif S[i] == "B":
        if i < (len(S) - 1):
            if S[i+1] == "A":
                flag = False
                break
    elif S[i] == "C":
        if i < (len(S) - 1):
            if S[i+1] == "A" or S[i+1] == "B":
                flag = False
                break

if flag:
    print("Yes")
else:
    print("No")