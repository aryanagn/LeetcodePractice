#LeetCode 1 -- Easy problem

#Dictionary
#Approach:
'''Initialize dictioanary named hmap to store elements of nums list along with its indices'''
'''loop over each element 'n' in 'nums' along with its corresponding index 'i'. Enumerate grabs both index and value of each element in list'''
'''Calculate difference of target minus n'''
'''if difference in the dictionary, return list of previously encountered element and current idx of element'''
'''add current element n as a key to the hmap dictionary with correspond idx value i to keep track of iteration'''
#Complexity
'''Time complexity: O(n)'''
'''Space complexity: O(n)'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hmap = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hmap:
            return [hmap[diff], i]
        hmap[n] = i


