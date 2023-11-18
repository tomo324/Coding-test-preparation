N = int(input())
S = input()

word_num = {}

counter = 1
for i in range(N):
    if i == N-1:
        if S[i] in word_num:
            word_num[S[i]] = max(counter, word_num[S[i]])
        else:
            word_num[S[i]] = counter
        break
    if S[i+1] == S[i]:
        counter += 1
    else:
        if S[i] in word_num:
            word_num[S[i]] = max(counter, word_num[S[i]])
        else:
            word_num[S[i]] = counter
        counter = 1

# word_numのすべての値を足して出力
print(sum(word_num.values()))