class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #does the annagram have to be an actual word? No
        #can the letters only be used once?character count must be same
        #BRUTE FORCE: iterate through each element of t and check if it exists
        #in s. if it doesnt, return False
        #length must be same for s and t. 


        if len(s)!=len(t):
            return False 

        hashS = dict()
        hashT = dict()
#building the hashmap - hashmaps have keys
        for i in range(len(s)):
            hashS[s[i]]= hashS.get(s[i],0) + 1
            hashT[t[i]]= hashT.get(t[i],0) + 1

# iterate through the keys of the hashmap and compare them

        return hashS == hashT

       
        



    



        

        