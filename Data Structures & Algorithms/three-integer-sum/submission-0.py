class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        ans = []

        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            l = i + 1
            r = len(s) - 1
            while l < r:
                total = s[i] + s[r] + s[l]
                if total == 0:
                    ans.append([s[i], s[l], s[r]])
                    l+= 1
                    while l < r and s[l] == s[l-1]:
                        l+= 1
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return ans