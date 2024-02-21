#LeetCode 242 -- EASY difficulty

#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#typically using all the original letters exactly once

#Approach
'''if lengths of two strings 's' and 't' not equal, return false immediately'''
'''initialize 2 dicts for occurrences of characters in strings: countS and countT'''
'''loop through each character of string 's' and string 't' using their indices and increment count for each '''
'''retrieve current count of character from dict, if it doesn't exist, then 0'''
'''compare strings if they are equal'''
#Complexity
'''Time complexity: O(n)'''
'''Space complexity: O(n)'''

def isAnagram(self, s: str, t:str)-> bool:
    if len(s)!= len(t):
        return False
    
    countS, countT= {},{}
    
    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i],0)
        countT[t[i]] = 1+countT.get(t[i],0)
        
    return countS == countT