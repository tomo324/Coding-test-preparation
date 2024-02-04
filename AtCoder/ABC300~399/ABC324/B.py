N = int(input())

ord_2 = 0
while N % pow(2, ord_2 + 1) == 0:
    ord_2 += 1

ord_3 = 0
while N % pow(3, ord_3 + 1) == 0:
    ord_3 += 1

if N == pow(2, ord_2) * pow(3, ord_3):
    print("Yes")
else:
    print("No")

