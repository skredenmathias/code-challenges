class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        # traverse array
        for i in range(len(nums)):
            elem = nums[i]
        # store element in cache as key: True
            if elem not in cache:
                cache[elem] = True
                # if we've reached the end of the list, and no duplicates, return False
                if len(cache) == len(nums):
                    return False
            else:
                return True