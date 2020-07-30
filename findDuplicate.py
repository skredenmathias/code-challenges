def findDuplicate(nums):
    # Make cache
    cache = {}
    # loop through array
    # store in cache as cache[num] = 1 , += 1
    for number in nums:
        if number not in cache:
            cache[number] = 1
        else:
            cache[number] += 1
    
    # check cache for a number with value > 1
    for number in nums:
        if cache[number] > 1:
            return number
    # return that number