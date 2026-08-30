class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_string = ""
        
        for char in s:
            binary_string += format(ord(char), '08b')
        
        return binary_string == binary_string[::-1]