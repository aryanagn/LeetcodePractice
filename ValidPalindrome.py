#Leetcode 125 -- EASY problem

#2 pointer method
#Approach:
'''convert string to lowercase letters only'''
'''build new string and check if each character is alphanumeric, if so add to string '''
'''define 2 pointers, left (l), and right (r) to keep track of traversing string'''
'''while loop to traverse pointers then compare if l and r are equal or not, if not return false'''
'''otherwise increment left pointer and decrement right pointer'''
'''if while loop is terminated, means that character at both of these pointers were never equal'''
#Complexity
'''each character visited once in string (linear) and extra constant space'''
'''Time complexity: O(n)'''
'''Space complexity: O(1)'''

def isValidPalindrome(self, s: str) -> bool:
    s = s.lower() 
    s = ''.join([c for c in s.lower() if c.isalnum()]) 
    l, r = 0, len(s) - 1
    
    while l<=r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True
