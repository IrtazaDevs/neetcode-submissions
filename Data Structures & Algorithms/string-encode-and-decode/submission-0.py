class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            size = len(word)
            result += chr(size) + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        while s:
            size = ord(s[0])
            word = s[1:size + 1]
            result.append(word)
            s = s[size + 1:]

        return result