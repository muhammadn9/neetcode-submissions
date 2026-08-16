class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pseudo
        # we need to create a prefix and suffix to get the multiplcation of 
        # everything to the left * everything to the right
        #initialize the prefix and suffix
        #iterate through the range
        #then save the answers to list output

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i -1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        output = [prefix[i] * suffix[i] for i in range(len(nums))]

        return output