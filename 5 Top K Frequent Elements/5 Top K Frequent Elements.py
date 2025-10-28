class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a frequency dictionary
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # sort items by frequency (highest first)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # take the first k numbers
        top_k = [num for num, freq in sorted_counts[:k]]
        return top_k