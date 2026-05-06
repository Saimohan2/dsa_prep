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

# """
# Given an array of integers temps where: temps[i] = temperature on day i
# Return an array res such that: res[i] = number of days you have to wait after day i to get a warmer temperature
# If there is no future day with a warmer temperature, set: res[i] = 0

# temps = [73,74,75,71,69,72,76,73]

# Output = [1,1,4,2,1,1,0,0]
# """

# def high_temp(temps):

#     res = [0]*len(temps)
#     stack = []

#     for i in range(len(temps)):

#         while stack and temps[i]>temps[stack[-1]]:

#             res[stack[-1]] = i-stack[-1]
#             stack.pop()

#         stack.append(i)
    
#     return res

# temps = [73,74,75,71,69,72,76,73]
# print(high_temp(temps))

# """
# Given a sorted array nums and a target,
# return the index of target. If not found → return -1

# nums = [-1,0,3,5,9,12]
# target = 9

# Output = 4
# """

# def bin_search(nums, target):

#     l = 0
#     r = len(nums)-1

#     while l<=r:

#         mid = (l+r)//2

#         if nums[mid]<target:
#             l = mid+1
        
#         elif nums[mid]>target:
#             r = mid-1
#         else:
#             return mid
#     return -1

# nums = [-1,0,3,5,10,12]
# target = 9
# print(bin_search(nums, target))

# """
# You are given an array: piles = [3,6,7,11] Each element represents a pile of bananas.
# You are also given an integer: h = 8 which represents the number of hours Koko has
# to finish eating.

# Rules
# Koko eats at a constant speed of k bananas per hour.
# Each hour, she chooses one pile and eats up to k bananas.
# If a pile has fewer than k bananas, she eats all of it and stops for that hour.

# Return the minimum integer k such that Koko can finish all bananas within h hours.

# """

# from math import ceil

# def hours_taken(piles, k, h):

#     hours_taken = 0
    
#     for p in piles:

#         hours_taken += ceil(p/k)
    
#     if hours_taken<=h:
#         return True

#     else: return False

# def min_speed(piles, h):

#     l = 1
#     high = max(piles)
#     answer = high

#     while l<=high:

#         mid = (l+high)//2

#         if hours_taken(piles, mid, h):
#             answer = mid
#             high = mid-1
        
#         else:
#             l = mid+1
#     return answer

# piles = [3,6,7,11]
# h = 8
# print(min_speed(piles, h))