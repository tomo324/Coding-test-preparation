# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        all_pattern = []
        one_list = [] # 編集せず常に保持

        for i in range(n):
            one_list.append(1)
        all_pattern.append(one_list)

        for i in range(len(one_list) - 1):
            tmp_list = one_list[:] # これを編集する
            a = tmp_list.pop(i)
            b = tmp_list.pop(i)
            c = a + b
            tmp_list.insert(i, c)
            all_pattern.append(tmp_list[:])
            print("tmp_list_1: {}".format(tmp_list))
            j = 0
            while j < (len(tmp_list) - 1):
                print(j)
                if tmp_list[j] == 1 and tmp_list[j + 1]  == 1:
                    a = tmp_list.pop(j)
                    b = tmp_list.pop(j)
                    c = a + b
                    tmp_list.insert(j, c)
                    all_pattern.append(tmp_list[:])
                    j += 1
                else:
                    j += 1
                print("tmp_list2: {}".format(tmp_list))
                print("all_pattern: {}".format(all_pattern))
        unique_all = list(map(list, set(map(tuple, all_pattern))))
        print(len(unique_all))
        return len(unique_all)

n = 6
solution = Solution()
climb = solution.climbStairs(n)





"""
n = 6


tmp_list = [1, 1, 1, 1, 1, 1]
i = 0
tmp_list = [2, 1, 1, 1, 1]
len(temp_list) -1 => 4
j = 0
[2, 1, 1, 1, 1]
j = 1
[2, 2, 1, 1]
j = 2
[2, 2, 2]







n = 5の時
1, 1, 1, 1, 1
2, 1, 1, 1,
2, 2, 1 #
2, 1, 2 #
1, 2, 1, 1
1, 2, 2 #
1, 1, 2, 1
2, 2, 1 #
1, 1, 1, 2
2, 1, 2 #
1, 2, 2 #

+ 18分

最初にすべて1の時のパターンをリストに入れる
次にインデックス０が２の時をforのネストで回して全パターンをリストに入れる
外のforによって任意の一か所が２になる
内側forの処理(range(len(one_list)- 1)):
if tmp_list[i] == 1 and tmp_list[i + 1]  == 1:
    s = tmp_list.pop(i) + tmp_list.pop(i + 1)
    tmp_list.insert(i, s)
    all_pattern.append(tmp_list)
内側のループ終了時に,すべてが１のリストにリセットして次の外側ループに入る


重複しているものを削除してリストのlengthを返す

リストが代入された変数を修正すると、その修正が代入元のリストにも反映されてしまう
リストの大きさをforループ内で変更する場合、rangeを使って固定回数回すべきではない
"""