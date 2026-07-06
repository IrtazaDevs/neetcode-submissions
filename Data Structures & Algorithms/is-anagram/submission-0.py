class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #does the annagram have to be an actual word?
        #can the letters only be used once?character count must be same
        #BRUTE FORCE: iterate through each element of t and check if it exists
        #in s. if it doesnt, return False
        
        return sorted(t) == sorted(s)

        