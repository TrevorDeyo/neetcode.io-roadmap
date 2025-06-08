# %% [markdown]
# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# 
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
# 
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
# 
# You can change the test parameters below :)

# %%
from typing import List
import random
import time
#from concurrent.futures import ThreadPoolExecutor, as_completed

# Test Case Generator
def generator():
    # Test Params
    numberofBatches = 20
    startingTestsPerBatch = 10
    rateofTestsPerBatchIncrease = 1.5
    maxIntValue = int("9" * 9)
    
    genTime = time.time()

    testBatches = []
    counter = 0
    for batchNum in range(numberofBatches):
        batchTime = time.time()
        if batchNum == 0:
            batchSize = startingTestsPerBatch
        else:
            batchSize *= int(rateofTestsPerBatchIncrease * (batchNum + 1))
        
        # build the batch
        testBatch = []
        for _ in range(int(batchSize)):
            testBatch.append(random.randint(0, maxIntValue))
        testBatches.append(testBatch)            

        print(f"\rTest Gen Batch {counter + 1} Complete, Time Elasped: {time.time() - batchTime:.5f} seconds.")
        counter += 1
    print(testBatches[0][0])
    print(f"Test Generator comeplete, time elasped: {time.time() - genTime:.5f} seconds")
    return testBatches        

# %%
def hasDuplicateBruteForce(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# %%
def hasDuplicateSorting(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


# %%
def hasDuplicateHashset(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# %%
def hasDuplicateHashsetLength(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)

# %%
def perfTest(func, testBatches):
    algoName = func.__name__
    perfTestTime = time.time()
    counter = 0
    detectedDuplicates = 0
    for batch in testBatches:
        batchTime = time.time()
        if func(batch):
            detectedDuplicates += 1
        print(f"Perf Test Batch{counter + 1} Complete - {algoName}, Time Elasped: {time.time() - batchTime:.5f} seconds.")
        counter += 1
    print(f"Detected: {detectedDuplicates} Batches with a duplicate int")
    print(f"Performance Test Complete, Time Elasped: {time.time() - perfTestTime:.5f} seconds.")
        

# %%
def main():
    mainTime = time.time()
    
    print("Performing Test Generation")
    testBatches = generator()

    print("Performing Performance Test")
    perfTest(hasDuplicateSorting, testBatches)
    perfTest(hasDuplicateHashset, testBatches)
    perfTest(hasDuplicateHashsetLength, testBatches)
    perfTest(hasDuplicateBruteForce, testBatches)

    print(f"Program Exec Complete... time elasped: {time.time() - mainTime:.5f} seconds.")

main()


