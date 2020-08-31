# Sliding window implementation
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Set initial window size
        k = 1
        cache = {}
        # loop through size on nums to try all window sizes
        for i in range(len(nums)):
            # search nums with window size k for subarray with largest sum
            for i in range(len(nums)):
                window = nums[i:k+i] # What if window edge crosses array edge?

                window_sum = sum(window)
                cache[i, k] = window_sum # index, window size
            # iterate window
            k += 1
        print(cache)
        key =  max(cache, key=cache.get)
        return cache[key]