class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BRUTE FORCE: add each number with next number indivually and record 
        #its index if it == target O(n2)
        #we can not use hashset since we want indices - so a hashmap
        
        hash = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff],i]
            hash[nums[i]]=i

    
                


        
            