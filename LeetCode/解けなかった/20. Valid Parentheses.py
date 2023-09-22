# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {"(":")", "{":"}", "[":"]"}
        stack = []
        if len(s) == 1:
            return False
        for strings in s:
            if strings in ["(", "{", "["]:
                stack.append(strings)
            else:
                if stack:
                    opening_character = stack.pop()
                    if s_dict[opening_character] != strings :
                        return False
                else:
                    return False
        if not stack:
            return True
        

'''
ヒントを見て解答

反省点
・s[-1]を使って最後の文字までを取得しようとしてしまった。この書き方だと最後の文字は無視される。
また、わざわざスライスを使う必要がない。
・開きかっこがスタックに無い場合にfalseを返す条件を入れるのを途中まで忘れていた。
・スタックの利用方法を知らなかった。データ構造の学習が必要。

'''