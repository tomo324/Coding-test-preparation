"""
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C&lang=ja

TLEになってしまった
"""

n = int(input())
command_list = [input() for _ in range(n)]

list = []

for command in command_list:
    if ' ' in command:
        space_index = command.index(' ')
        cmd = command[:space_index]
        value = command[space_index + 1:]
    else:
        cmd = command
        value = None
    if cmd == 'insert':
        list.insert(0, value)
    elif cmd == 'delete':
        if value in list:
            list.remove(value)
    elif cmd == 'deleteFirst':
        del list[0]
    elif cmd == 'deleteLast':
        list.pop()

print(' '.join(list))