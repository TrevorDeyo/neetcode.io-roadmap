import heapq
import random
import time

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a frequency dictionary
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # sort items by frequency (highest first)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # take the first k numbers
        top_k = [num for num, freq in sorted_counts[:k]]
        return top_k
    
    def topKFrequentMinHeap(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                

def generate_test_case(size: int, value_range: int, k: int):
    nums = [random.randint(0, value_range) for _ in range(size)]
    return nums, k

def time_function(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

sol = Solution()

nums, k = generate_test_case(size=100000, value_range=1000, k=10)

res1, t1 = time_function(sol.topKFrequent, nums, k)
res2, t2 = time_function(sol.topKFrequentMinHeap, nums, k)
res3, t3 = time_function(sol.topKFrequentBucketSort, nums, k)

print(f"Sorting version:     {t1:.6f} seconds")
print(f"Min-Heap version:    {t2:.6f} seconds")
print(f"Bucket Sort version: {t3:.6f} seconds")
