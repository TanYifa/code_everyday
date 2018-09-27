
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

 
class Solution_q1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        residual = [target-x for x in nums]
        N = len(nums)
        for i in range(N):
            for k in range(i+1,N):
                if residual[k] == nums[i]:
                    return [i,k]
        return None
       
#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#Example 2:

#Input: -123
#Output: -321
#Example 3:

#Input: 120
#Output: 21
#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
        
class Solution_q2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        list_x = list(str(x))
        if list_x[0] == '-':
            negative = True
            list_x = list_x[1:]

        while(len(list_x) > 1 and list_x[-1] == '0'):
            list_x.pop()

        N = len(list_x)
        for i in range(round(N/2)):
            list_x[i], list_x[N-i-1] =  list_x[N-i-1],  list_x[i]

        result = ''
        for _ in list_x:
            result += _
        result = int(result)

        if negative:
            result = -1*result
        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result
''' 
# 3 lines solution
class Solution():
    def reverse(self, x):
        sign = [1, -1][x < 0]   # [1, -1][False] is 1, [1,-1][True] is -1
        result = sign*int(str(abs(x))[::-1])  # Dont forget basic
        return result if - 2**31 < result < 2**31 else 0
 '''

