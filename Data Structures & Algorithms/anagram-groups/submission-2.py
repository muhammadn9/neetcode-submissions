class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

            
        return list(groups.values())


        # Initialize a hashmap
        # iterate through list of words
        # for each word, sort its characters to create a "key" (anagrams sort to the same key)
        # if key doesn't exist in hashmap, create empty list for it
        # append the word to the list at that key
        # once iteration is complete, return all the hashmap's values as the result

        