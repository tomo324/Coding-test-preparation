S = input()
ans = ""

for s in S:
    if "a" not in s and "e" not in s and "i" not in s and "o" not in s and "u" not in s:
        ans += s

print(ans)