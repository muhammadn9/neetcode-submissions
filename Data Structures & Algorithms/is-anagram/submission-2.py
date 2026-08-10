class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        
        for char in s :
            counts[char] = counts.get(char, 0) + 1

        for char in t :
            counts[char] = counts.get(char, 0) - 1

        for val in counts.values():
            if val != 0 :
                return False
        
        return True


        # check to see if string s equals string t;
        # create hashmap
        # go through string S and add value count to the hashmap for each letter
        # go through string T and remove value count from the Hashmap for each letter.
        # If hashmap values added together = 0, then return true, otherwise false.