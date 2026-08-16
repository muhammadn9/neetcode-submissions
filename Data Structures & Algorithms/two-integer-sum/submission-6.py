class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []