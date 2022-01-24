
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        #bascically remove each character and check if we have a palindrome
        #define left and right pointers to start from both edges
        #if mismatch
        #remove left and check for palindrome
        #remove right and check for palindrome
        #move left and right and redo the checks


        left = 0
        right = len(s) - 1
        
        while(left<right):
            
            if(s[left] != s[right]):
                
                removeLeft = s[left+1:right+1]
                removeRight = s[left:right]

                return self.isPalindrome(removeLeft) or self.isPalindrome(removeRight)

            left +=1
            right -=1
        
        return True
    
    def isPalindrome(self, s:str) -> bool:
        return s == s[::-1]
    
