#LeetCode 217 --- EASY difficulty

#HashSet
#Approach
'''Use hash set to store nums'''
'''loop through num in list nums'''
'''if num encountered in hash set, return True'''
'''add that num to the hash set to keep track'''
'''otherwise return false'''

def containsDuplicate(self, nums: List[int])-> bool:
    hmap = set()
    for num in nums:
        if num in hmap:
            return True
        hmap.add(num)
    return False