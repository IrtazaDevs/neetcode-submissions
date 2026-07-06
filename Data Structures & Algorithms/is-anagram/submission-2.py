class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False 

        hashS = dict()
        hashT = dict()
#building the hashmap - hashmaps have keys
        for i in range(len(s)):
            hashS[s[i]]= hashS.get(s[i],0) + 1
            hashT[t[i]]= hashT.get(t[i],0) + 1
#iterating through the keys of the hashmap now
        for c in hashS:
            if hashS[c]!= hashT.get(c):
                return False
            
        return True
