def uncover_spy(n, trust):
    cache = {}
    trusted_arr = []
    possible_spies = []
    for lst in trust:
        trustee = lst[0]
        trusted = lst[1]
        # Spy will be trusted by everyone
        trusted_arr.append(trusted)

        if trustee not in cache:
            cache[trustee] = [trusted]
        else:
            cache[trustee].append(trusted)
            
    # print(cache)
    
    for possible_spy in range(1, n + 1):
        # Spy would not be key in cache
        if possible_spy not in cache:
            # print(possible_spy)
            print('trusted arr ', trusted_arr)
            if trusted_arr.count(possible_spy) == n - 1:
                possible_spies.append(possible_spy)

    # If only one spy
    print(len(possible_spies))
    if len(possible_spies) == 1:
        return possible_spies[0]
    else:
        return -1