def total(n):
    if n < 1:
        return 0
    return n + total(n-1)


def double_list(lst):
    if lst == []:
        return []
    first = lst[0]
    rest = lst[1:]
    return [first * 2] + double_list(rest)

def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)


