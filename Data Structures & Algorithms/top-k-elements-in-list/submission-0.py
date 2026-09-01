class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_element = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] = counter[num] + 1
        sorted_counter = sorted(counter.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            freq_element.append(sorted_counter[i][0])
        return freq_element