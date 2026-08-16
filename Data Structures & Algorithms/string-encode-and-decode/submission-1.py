class Solution:

    def encode(self, strs: List[str]) -> str:
    
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s
        # s = "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        
        while left < len(s):
            j = s.find("#", left)
            length = int(s[left:j])
            word = s[j+ 1: j + 1 + length]
            res.append(word)
            left = j + 1 + length
        return res


# create a string and add to it the len of the first word + # + word

#for the decode we need to locate the #, take the number behind it as the len
# go len(int) past # and save that as the first str 
# append the str to a list and return the list