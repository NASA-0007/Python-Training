class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPal(i + 1, j) or isPal(i, j - 1)
            i += 1
            j -= 1
        return True