S = input()
max_len = 1

for i in range(len(S)):
    for j in range(i, len(S)):
        a = S[i:j+1]
        reversed_a = a[::-1]
        if a == reversed_a:
            max_len = max(max_len, len(a))

print(max_len)