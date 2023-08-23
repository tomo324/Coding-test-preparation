words = ["dream", "dreamer", "erase", "eraser"]

s = input()

s = s[::-1]
for i in range(4):
    words[i] = words[i][::-1]

can = True
i = 0

while i < len(s):
    can2 = False
    for word in words:
        if s[i:i + len(word)] == word:
            can2 = True
            i += len(word)
            break
    if not can2:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")