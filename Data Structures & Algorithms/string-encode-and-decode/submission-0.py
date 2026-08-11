class Solution:
    def encode(self, strs: List[str] ) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            j = s.find("#", left)
            length = int(s[left:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            left = j + 1 + length
        return res