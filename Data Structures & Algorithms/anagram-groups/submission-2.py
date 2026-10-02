class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #can the sublist be of any size? for example out of 5 strings, 4 in 1 sublist and 1 in another sublist?
        #all anagrams inside one sublist

        hash = defaultdict(list)

        for s in strs:
            char = [0] * 26 #small a.....z . 26 values
            for c in s:
                char[ord(c) - ord("a")] +=1
            hash[tuple(char)]. append(s)
        
        return list(hash.values())