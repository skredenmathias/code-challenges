class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = []
        cache = {}

        for char in s:
            if char in longest_substring:
                cache[len(longest_substring)] = longest_substring
                longest_substring = []

            if char not in longest_substring:
                longest_substring.append(char)
        
        return max(cache.keys())