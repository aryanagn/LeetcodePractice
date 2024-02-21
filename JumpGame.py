#LeetCode 55 -- MEDIUM difficulty


#Approach 
'''initialize goal to idx of last element in nums list. This goal represents idx that needs to be reached to determine if it is possible to jump to end of list'''
'''loop to iterate backward through indices of nums list, starting from second to last element down to 0, decrementing by 1 in each iteration'''
'''check if curr idx i + value at that idx nums[i] is >= to 'goal'. If true, it is possible to from from idx i to reach goal'''
'''if previous cond true, update goal to curr idx'''
'''return true if goal has reached idx 0, indicating it is possible to jump from beginning of list to end, else false'''
#Complexity
'''Time complexity: O(n)'''
'''Space complexity: O(1)'''

def canJump(self, nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums)-2,-1,-1):
        if i + nums[i]>=goal:
            goal = i
    return goal == 0