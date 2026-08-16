class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for c in strs:
            sorted_word = ''.join(sorted(c))
            if sorted_word not in seen:
                seen[sorted_word] = [] 
            seen[sorted_word].append(c)
        return list(seen.values())