class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        ans = 0
        if num < 0:
            return False
        while num != 0:
            digit = num % 10
            num = num // 10
            ans = ans * 10 + digit
        return ans == x