def twoSum(arr, target):
    cache = {}
# iterate over indices
    for i in range(len(nums)):
        # store element in cache[elem] = i
        elem = nums[i]
        cache[elem] = i
    # iterate again over indices
    print(cache)
    for i in range(len(nums)):
    # check if current elem + item in cache adds up to target
    # also check if indeces are the same, if so, disregard.
        elem = nums[i]
        if target - elem in cache and i != cache[target - elem]:
            cached_value_index = cache[target - elem]
            indeces = [i, cached_value_index]
            return indeces