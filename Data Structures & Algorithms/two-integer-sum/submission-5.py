class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}

        for i, num in enumerate(nums):
            result = target - num
            if result in exists:
                return [exists[result], i]
            exists[num] = i
        return []