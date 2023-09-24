abcd = input()

for i in range(2 ** 3):
    op = ["-", "-", "-"]
    for j in range(3):
        if ((i >> j) & 1):
            op[j] = "+"
    
    formula = ""
    formula += abcd[0] + op[0] + abcd[1] + op[1] + abcd[2] + op[2] + abcd[3]
    if eval(formula) == 7:
        print(formula + "=7")
        break