def coin(money):
    c_10 = money // 10
    rest = money % 10
    c_5 = rest // 5
    c_1 = rest % 5
    print(f"10円玉{c_10}枚、５円玉{c_5}枚、1円玉{c_1}枚")


money = int(input())
if money <= 49:
    coin(money)
else:
    print("その金額の金種は計算できません")