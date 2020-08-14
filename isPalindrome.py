class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Given int, check if palindrome. Returns bool.
        
        string_int = ' '.join(str(x)).split()
        string_int_copy = string_int.copy()
        string_int_copy.reverse()
        
        if string_int == string_int_copy:
            return True
        else:
            print(string_int)
            print(string_int_copy)
            return False