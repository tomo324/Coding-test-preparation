all_pattern = [1, 1]
one_list = [1, 1] # 編集せず常に保持
tmp_list = [] # ここを編集

tmp_list = one_list

tmp_list.pop(0)

print(tmp_list)
print(one_list)

list = [[1, 1], [1, 2, 3], [1, 1]]
duplicates = set(list)
print(duplicates)