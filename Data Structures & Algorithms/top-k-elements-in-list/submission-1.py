import heapq
class Solution:
    
    def get_frequency(self, nums: List[int]) -> Dict:
        freq_dict = {}
        
        for item in nums:
            if item not in freq_dict:
                freq_dict[item] = 1
            else:
                freq_dict[item] += 1

        return freq_dict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = []
        freq_dict = {}
        inverse_dict = {}

        freq_dict = self.get_frequency(nums)

        frequencies = []

        for key in freq_dict:
            value = freq_dict[key]
            frequencies.append(value)
        
        max_heap = [-k for k in frequencies]
        heapq.heapify(max_heap)

        for i in range(k):
            top = -1 * heapq.heappop(max_heap)

            for key in freq_dict:
                value = freq_dict[key]
                if value == top and key not in answer:
                    answer.append(key)
        return answer