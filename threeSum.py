#3Sum
'''
https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

class Solution(object):
    def threeSum(self, nums):
        answer=[]
        answer_list=[]
        if len(nums)<3:
            return answer_list
        else:
            for i,n in enumerate(nums):
                nums2 = nums[0:i]+nums[i+1:]
                for i,m in enumerate(nums2):
                    nums3 = nums2[0:i]+nums2[i+1:]
                    for v in nums3:
                        if v==0-(n+m):
                            answer=sorted([n,m,v])
                    if answer!=answer_list and answer not in answer_list:
                        answer_list.append(answer)
            return answer_list
            