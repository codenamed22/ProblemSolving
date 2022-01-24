
"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #go from left to right
        #if we find an opening bracket, put the index into the stack
        #if we find a closing bracket, pop from stack to check if we had a opening bracket
        #if yes, then fine, if not, mark for deletion
        #at the end delete all un needed opening brackets and marked indexes
        
        stack = []
        delete = set()
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    delete.add(i)
                else:
                    stack.pop()
                    
        delete = delete.union(set(stack))
        
        res = []
            
        for i,c in enumerate(s):
            if i not in delete:
                res.append(c)
                
        return "".join(res)
                    
