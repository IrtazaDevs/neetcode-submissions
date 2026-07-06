import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        remove_map = str.maketrans('', '', string.punctuation + string.whitespace)
        s = s.translate(remove_map)

        x = s[::-1]
        
        if x == s:
            return True
        return False

    
        