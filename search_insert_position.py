class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # given sorted array and target
            # return index if target found
            # else:
                # return where it would be
                
        for i in range(len(nums)):
            element = nums[i]
            print(i)
            # if element is smaller, go next
            if element < target and i - 1 < len(nums):
                continue            
                
            # if element is equal, return it
            if element == target:
                return i
            
            # if element is larger, return previous index
            if element > target:
                return i
            
            # if target is not in array
            else:
                return len(nums)