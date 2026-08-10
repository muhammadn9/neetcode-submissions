class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # Create a new hashMap
        # we're going to iterate through the nums array, take the target number, 
        # subtract the value of the index from the target,
        # then search for the result in the nums array.
        # if we find the answer,
        # return the initial index and the result index,
        # else add to the hashmap and continue onto next index.

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
        return []