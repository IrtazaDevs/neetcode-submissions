class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

#brute force: WE check every element of the array against every other element
#are all numbers always going to be sorted?
#Core action: has this number appeared already? So what DS can I use? (instant lookup)
#Can we use a hashmap? but that would be inefficient for the memory and we dont need it
#Lets use a hash set

        #initialize hashset
        hash = set()
        for i in nums:
            if i in hash:
                return True
            hash.add(i)
        return False
