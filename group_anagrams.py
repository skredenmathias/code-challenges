def groupAnagrams(strs):
    answer = []
    for i in range(len(strs)):
        #set a cur pointer at the word
        cur = strs[i]
        # set a pointer at the next word
        next_word = strs[i+1]
        #init a sublist
        temp_list = []
        while next_word:
            if list(cur) == list(next_word):
                temp_list.append(cur)
                temp_list.append(next_word)
            cur = next_word
            next_word = strs[i+2]
        answer.append(temp_list)
    return answer