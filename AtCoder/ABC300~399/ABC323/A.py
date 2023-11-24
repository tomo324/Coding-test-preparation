s = input()
judge = True

for i in range(16):
    if (i+1) % 2 == 0 and s[i] != "0":
        judge = False

if judge:
    print("Yes")
else:
    print("No")