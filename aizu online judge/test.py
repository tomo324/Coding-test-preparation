import sys

class MenuInfo:
    def __init__(self, food_num, stock, price):
        self.food_num = food_num
        self.stock = stock
        self.price = price

class OrderInfo:
    def __init__(self, table, food_num, order_num):
        self.table = table
        self.food_num = food_num
        self.order_num = order_num



def main(lines):
    menu_list = []
    order_list = []
    step = int(lines[0])
    m = int(lines[1])
    for i in range(2, 2 + m):
        d, s, p = map(int, lines[i].split())
        menu_info = MenuInfo(d, s, p)
        menu_list.append(menu_info)
    for i in range(2 + m, len(lines)):
        info_list = lines[i].split()
        t = int(info_list[1])
        d = int(info_list[2])
        n = int(info_list[3])
        order_info = OrderInfo(t, d, n)
        order_list.append(order_info)
    print(menu_list)
    print(order_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)









import sys

class MenuInfo:
    def __init__(self, food_num, stock, price):
        self.food_num = food_num
        self.stock = stock
        self.price = price

class OrderInfo:
    def __init__(self, table, food_num, order_num):
        self.table = table
        self.food_num = food_num
        self.order_num = order_num

step = 0
m = 0
menu_list = []
order_list = []

def main(lines):
    for i, v in enumerate(lines):
        if i == 0:
            step = int(v)
        if i == 1:
            m = int(v)
        if 1 < i <= m + 1:
            d, s, p = map(int, v.split())
            menu_info = MenuInfo(d, s, p)
            menu_list.append(menu_info)
        if i > m + 1:
            info_list = v.split()
            t = int(info_list[1])
            d = int(info_list[2])
            n = int(info_list[3])
            order_info = OrderInfo(t, d, n)
            order_list.append(order_info)
    print(menu_list)
    print(order_list)
        

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
