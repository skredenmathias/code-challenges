def first_not_repeating_character(s):
    # loop through string and add to cache as cache[letter] = 1
    lst = list(s)
    cache = {}
    for letter in lst:
        if letter not in cache:
            cache[letter] = 1
        else:
            cache[letter] += 1
    print(cache)

    non_repeat = None
    count = 0
    print(len(lst))
    while non_repeat == None:
        letter = s[count]
        print(letter)
        if cache[letter] < 2:
            non_repeat = letter
            return non_repeat
        count += 1
        if count >= len(lst):
            return '_'