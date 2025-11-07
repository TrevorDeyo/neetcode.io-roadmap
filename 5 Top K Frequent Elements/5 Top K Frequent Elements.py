import heapq
import random
import time
import tracemalloc
from typing import List

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

def measure_performace(func, *args):
    # Start timing and memory tracking
    tracemalloc.start()
    start = time.perf_counter()

    result = func(*args)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "result": result,
        "time": end - start,
        "memory_peak_kb": peak / 1024
    }

sol = Solution()
nums, k = generate_test_case(size=1000000, value_range=100, k=10)

perf_sorting = measure_performace(sol.topKFrequent, nums, k)
perf_heap = measure_performace(sol.topKFrequentMinHeap, nums, k)
perf_bucket = measure_performace(sol.topKFrequentBucketSort, nums, k)

print(f"Sorting version:     {perf_sorting['time']:.6f} s, {perf_sorting['memory_peak_kb']:.2f} KB peak")
print(f"Min-Heap version:    {perf_heap['time']:.6f} s, {perf_heap['memory_peak_kb']:.2f} KB peak")
print(f"Bucket Sort version: {perf_bucket['time']:.6f} s, {perf_bucket['memory_peak_kb']:.2f} KB peak")
