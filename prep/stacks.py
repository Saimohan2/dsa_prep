# """
# Given an array nums, for each element, find the next greater element to its right.
# If none exists, return -1.

# nums = [2,1,2,4,3]

# Output = [4,2,4,-1,-1]
# """

# def next_greatest(nums):

#     n = len(nums)
#     res = [-1]*n
#     stack = []

#     for i in range(n):

#         while stack and nums[i]>nums[stack[-1]]:

#             res[stack[-1]] = nums[i]
#             stack.pop()
        
#         stack.append(i)
#     return res

# nums = [2,1,2,4,3]
# print(next_greatest(nums))