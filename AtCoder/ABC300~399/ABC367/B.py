X = input()

while True:
    if X[-1] == "0":
        X = X[:-1]
    elif X[-1] == ".":
        X = X[:-1]
        break
    else:
        break

print(X)