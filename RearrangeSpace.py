#1592. Rearrange Spaces Between Words
#You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
#Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
#Return the string after rearranging the spaces.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = sum(1 for i in text if i==' ')
        words = [words for words in text.split() if words]

        if len(words) > 1:
            space_div = space_count // (len(words) - 1)
        else:
            space_div = 0
        
        extra_space_count = space_count % (len(words) - 1) if len(words) > 1 else space_count
        output = ((" ")*space_div).join(words)
        output += extra_space_count*" "
        
        return(output)
