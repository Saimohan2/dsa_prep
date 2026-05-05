# """
# Problem:
# Given a string s, find the length of the longest substring 
# without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: "abc"
# """

# def longest_subs(s):

#     l = 0
#     f = {}
#     maxl = 0
#     n = len(s)

#     for r in range(n):

#         f[s[r]] = f.get(s[r], 0) +1

#         while f[s[r]]>1 and l<=r:

#             f[s[l]] = f.get(s[l], 0) -1

#             if f[s[l]] == 0:
#                 del f[s[l]]
            
#             l = l+1
#         maxl = max(maxl, r-l+1)
#     return maxl

# s = "abcaaaaa"
# print(longest_subs(s))


# """
# Given an array of positive integers nums and an integer k,
# return the length of the longest subarray such that:

# nums = [2,1,5,1,3,2], k = 7
# Output: 4
# Explanation: [1,5,1] or [5,1,1] etc.
# """

# def max_len(nums, k):

#     l = 0
#     maxl = 0
#     currsum = 0

#     for r in range(len(nums)):
#         currsum += nums[r]

#         while currsum>k and l<=r:
#             currsum = currsum - nums[l]
#             l += 1
        
#         maxl = max(maxl, r-l+1)
    
#     return maxl

# nums = [2,1,5,1,3,2]
# k = 7

# print(max_len(nums, k))

# """
# Given an array of positive integers nums and integer k,
# return the number of subarrays whose sum is ≤ k.

# nums = [1,2,3]
# k = 3

# Output: 4

# Valid subarrays:
# [1], [2], [3], [1,2]
# """

# def count_sub(arr, k):

#     l = 0
#     currsum = 0
#     count = 0

#     for r in range(len(arr)):
#         currsum += arr[r]

#         while currsum>k and l<=r:
#             currsum -= arr[l]
#             l += 1

#         count += r-l+1

#     return count

# arr = [3,1,0]
# k = 3
# print(count_sub(arr, k))

# """
# Given a string s and integer k, return the length of the
# longest substring with at most k distinct characters.

# s = "eceeeba"
# k = 2

# Output: 3  # "ece"
# """

# def distinct_char(st, k):

#     l = 0
#     maxlen = 0
#     f = {}

#     for r in range(len(st)):
#         f[st[r]] = f.get(st[r], 0)+1

#         while len(f)>k and l<=r:
#             f[st[l]] = f.get(st[l], 0)-1
#             if f[st[l]] == 0:
#                 del f[st[l]]
            
#             l += 1
        
#         maxlen = max(maxlen, r-l+1)
    
#     return maxlen

# st = "eceeeeeba"
# k = 2

# print(distinct_char(st, k))

# """
# Given a string s and integer k,
# return the number of substrings with exactly k distinct characters.

# s = "pqpqs"
# k = 2

# Output: 7
# """

# def at_most(st, k):

#     l = 0
#     count = 0
#     f = {}

#     for r in range(len(st)):
#         f[st[r]] = f.get(st[r], 0)+1

#         while len(f)>k and l<=r:
#             f[st[l]] = f.get(st[l], 0)-1

#             if f[st[l]] == 0:
#                 del f[st[l]]

#             l += 1
#         count += r-l+1
#     return count

# def exactly_k(st, k):

#     return at_most(st,k)-at_most(st, k-1)

# st = "pqpqs"
# k = 2

# print(exactly_k(st, k))


# """
# Given an integer array nums, return the maximum subarray sum.

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output = 6  # [4,-1,2,1]
# """

# def maxsum(nums):

#     cursum = 0
#     max_sum = float("-inf")

#     for i in range(len(nums)):

#         cursum = max(nums[i], cursum+nums[i])

#         max_sum = max(max_sum, cursum)

#     return max_sum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxsum(nums))


# """
# Find the maximum subarray sum after at most one deletion

# nums = [5, -1, -2, 10]
# expected: 15

# d k m 0 5 5, 5 4 5, 4 2 5, 14 12 14
# """

# def deletion(nums):

#     keep = nums[0]
#     drop = float("-inf")
#     maxs = nums[0]

#     for i in range(1, len(nums)):

#         drop = max(keep, drop+nums[i])
#         keep = max(nums[i], keep+nums[i])

#         maxs = max(maxs, keep, drop)

#     return maxs

# nums = [5, -1, -2, 10]
# print(deletion(nums))


# """
# Given a sorted array nums and an integer target,
# return True if there exists a pair (i, j) such that:

# nums = [1, 2, 3, 4, 6]
# target = 6

# Output: True   # because 2 + 4 = 6
# """

# def twosum_check(nums, target):

#     l = 0
#     r = len(nums)-1

#     while l<r:

#         if nums[l]+nums[r]>target:
#             r -= 1
        
#         elif nums[l]+nums[r]<target:
#             l+=1

#         else:
#             return True

#     return False

# nums = [1, 2, 3, 5, 6]
# target = 6
# print(twosum_check(nums, target))


# """
# Given a sorted array, return the indices (1-based) of two numbers such that:
# nums[i] + nums[j] == target

# nums = [2, 7, 11, 15]
# target = 9

# Output: [1, 2]
# """

# def twosum_idx(nums, target):

#     l = 0
#     r = len(nums)-1

#     while l<r:

#         if nums[l]+nums[r]>target:
#             r -= 1
        
#         elif nums[l]+nums[r]<target:
#             l += 1

#         else:
#             return [l+1, r+1]
    
#     return []

# nums = [2, 7, 11, 15]
# target = 9

# print(twosum_idx(nums, target))


# """
# Given an unsorted array, return indices such that: nums[i] + nums[j] == target

# nums = [2, 7, 11, 15]
# target = 9

# Output: [0, 1]
# """

# def two_sum(nums, target):

#     seen = {}

#     for i in range(len(nums)):

#         comp = target - nums[i]

#         if comp in seen:
#             return [seen[comp], i]
        
#         seen[nums[i]] = i
    
#     return []

# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))

# """
# Given a string s, return the length of the longest substring without repeating characters.

# s = "abcabcbb"
# Output = 3   # "abc"
# """

# def non_repeating(str):

#     l = 0
#     maxlen = 0
#     f = {}
#     n = len(str)

#     for r in range(n):

#         f[str[r]] = f.get(str[r], 0)+1

#         while f[str[r]]>1:
#             f[str[l]] = f.get(str[l], 0)-1

#             if f[str[l]] == 0:
#                 del f[str[l]]

#             l += 1
        
#         maxlen = max(maxlen, r-l+1)
    
#     return maxlen

# str = "abcdabcbb"
# print(non_repeating(str))


# """
# Given an array of positive integers nums and integer k,
# return the length of the longest subarray such that: sum<=k

# nums = [2,1,5,1,3,2]
# k = 7
# Output = 3
# """

# def long_sub(nums, k):

#     l = 0
#     maxl = 0
#     cursum = 0

#     for r in range(len(nums)):

#         cursum += nums[r]

#         while cursum>k and l<=r:

#             cursum -= nums[l]
#             l += 1

#         maxl = max(maxl, r-l+1)

#     return maxl

# nums = [2,1,3,1,3,2]
# k = 7
# print(long_sub(nums, k))


"""
Given an array nums, return all unique triplets such that: nums[i] + nums[j] + nums[k] == 0

nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2],
 [-1,  0, 1]]
"""

# def three_sum(nums):

#     nums.sort()
#     res = []
#     n = len(nums)

#     for i in range(n):

#         if i > 0 and nums[i] == nums[i-1]:
#             continue
        
#         l = i+1
#         r = n-1

#         while l<r:

#             if nums[i]+nums[l]+nums[r]>0:
#                 r -= 1
            
#             elif nums[i]+nums[l]+nums[r]<0:
#                 l +=1
            
#             else:
#                 res.append([nums[i], nums[l], nums[r]])
#                 l += 1
#                 r -= 1

#                 while l<r and nums[l] == nums[l-1]:
#                     l += 1
            
#                 while l<r and nums[r] == nums[r+1]:
#                     r -= 1
    
#     return res

# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))


# """
# Given an integer array nums, find the maximum sum of a contiguous subarray.

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# Output = 6
# """

# def kadane_max(nums):

#     cursum = nums[0]
#     maxsum = nums[0]

#     for i in range(1, len(nums)):

#         cursum = max(nums[i], cursum+nums[i])
#         maxsum = max(maxsum, cursum)

#     return maxsum

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# print(kadane_max(nums))



"""
Given an array nums, you can delete at most one element,
return the maximum subarray sum.

nums = [1, -2, 0, 3]

Output = 4
"""

# def best_del(nums):

#     keep = nums[0]
#     drop = 0
#     maxsum = nums[0]

#     for i in range(1,len(nums)):

#         drop = max(keep, drop+nums[i])
#         keep = max(nums[i], keep+nums[i])
#         maxsum = max(maxsum, keep, drop)

#     return maxsum

# nums = [1, -4, -2, 0, 3]
# print(best_del(nums))