class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        for s in strs[1:]:
            while not s.startswith(base):
                base = base[:-1]
        if base:
            return base
        else:
            return ""
        
# スライスの使い方をマスターする
# startswithなどの便利なメソッドを知っておく。知らなければ検索してみる