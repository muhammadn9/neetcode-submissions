class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = [c for c in s if c.isalnum()]
        l = 0
        r = len(filtered) - 1

        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l+= 1
            r-= 1
        return True
            