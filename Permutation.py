"""

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


"""



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #if s1 is bigger, false
        #create a list of size 26 with each location representing a - z and the number is the freq
        #move across first string and populate list 1
        #move across 2nd string, each character we encounter we increase it in the second list
        #once we move out of our window size (len of s1) we start decreasing the character we just left
        #compare the two lists, return true if they are equal
        
        if len(s1) > len(s2):
            return False
        
        ls1 = [0]*26
        ls2 = [0]*26
        
        for i in range(len(s1)):
            ls1[ord(s1[i]) - 97]+=1
        
        for i in range(len(s2)):
            ls2[ord(s2[i]) - 97]+=1
            
            if i > len(s1)-1:
                ls2[ord(s2[i-len(s1)]) - 97]-=1
            
            if ls1 == ls2:
                return True
            
        return False
