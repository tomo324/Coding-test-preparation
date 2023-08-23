n = input()
count = 0
for i in range(len(n)):
    if n[i] == "1":
        count += 1
print(count)