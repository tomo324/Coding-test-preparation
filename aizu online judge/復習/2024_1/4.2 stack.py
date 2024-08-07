A = input()
A_list = A.split()

stack = []

for i in range(len(A_list)):
    if A_list[i] in ['+', '-', '*']:
        a = stack.pop()
        b = stack.pop()
        stack.append(eval(str(b) + A_list[i] + str(a)))
    else:
        stack.append(A_list[i])

print(stack[0])