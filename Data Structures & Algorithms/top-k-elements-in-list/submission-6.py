class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # psuedo
        # first create a hashMap
        # hashMap will store the number of occurences for each num
        # then we create a heap
        # for heap, we will pop out the value if we have more values than k
        # then remaining values will be appened to a new list called ans
        # we will specifically save the most occuring number, not number of 
        # occurance

        count = defaultdict(List)

        for n in nums:
                count[n] = count.get(n, 0) + 1
        
        heap = []
        for n in count.keys():
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans