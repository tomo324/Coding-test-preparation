s = input()

reversed_word = []
result = 0

for i in range(len(s)):
    for j in range(len(s)):
        w = s[i:j+1]
        reversed_word = w[::-1]
        if w == reversed_word and len(w) > result:
            result = len(w)

print(result)