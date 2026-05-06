# """
# Given an array nums and an integer k,
# return the number of subarrays whose sum equals k.

# nums = [1,1,1]
# k = 2

# Output = 2
# """

# def subarray_sum(nums, k):
    
#     count = 0
#     seen = {0:1}
#     cursum = 0

#     for i in range(len(nums)):

#         cursum += nums[i]

#         if cursum-k in seen:
#            count += seen[cursum-k]
        
#         seen[cursum] = seen.get(cursum, 0)+1

#     return count

# nums = [0,0,0]
# k = 0
# print(subarray_sum(nums, k))


# """
# Given an integer array nums and an integer k,
# return the length of the longest subarray whose sum equals k.

# nums = [1, -1, 5, -2, 3]
# k = 3

# Output = 4
# """

# def longest_sub(nums, k):
    
#     cursum = 0
#     seen = {0:-1}
#     maxl = 0

#     for i in range(len(nums)):

#         cursum += nums[i]

#         if cursum-k in seen:
#             l = i-seen[cursum-k]
#             maxl = max(maxl, l)

#         if cursum not in seen:
#             seen[cursum] = i
    
#     return maxl

# nums = [1, -1, 0, 5, -2, 3]
# k = 3
# print(longest_sub(nums, k))


# """
# Best Time to Buy and Sell Stock

# You are given an array: prices[i] = price of stock on day i

# prices[i] = price of stock on day i

# You want to maximize profit by:

# Buying on one day
# Selling on a later day

# Return the maximum profit. If no profit possible → return 0

# prices = [7,1,5,3,6,4]

# Output = 5
# """

# def max_prof(prices):

#     max_profit = 0
#     min_price = prices[0]

#     for i in range(len(prices)):

#         profit = prices[i]-min_price

#         min_price = min(min_price, prices[i])

#         max_profit = max(profit, max_profit)
    
#     return max_profit

# prices = [7,1,10,3,6,4]
# print(max_prof(prices))

# """
# You are given: prices[i] = price on day i

# You can:

# Buy and sell multiple times
# But cannot hold more than one stock at a time
# You must sell before buying again

# Return the maximum profit

# prices = [7,1,5,3,6,4]

# Output = 7
# """

# def mprof(prices):

#     profit = 0

#     for i in range(1, len(prices)):

#         if prices[i]>prices[i-1]:
#             profit += prices[i]-prices[i-1]

#     return profit

# prices = [7,1,5,3,6,4]
# print(mprof(prices))


# """
# Given a string s containing just the characters:( ) { } [ ]

# Determine if the input string is valid.

# A string is valid if:
# Every opening bracket has a corresponding closing bracket
# Brackets are closed in the correct order
# Each closing bracket matches the same type of opening bracket

# s = "()"
# Output: True
# """

# def is_valid(s):

#     stack = []
#     mapping = {'}':'{', ']': '[', ')': '('}

#     for c in s:

#         if c in mapping:
#             if not stack or stack[-1] != mapping[c]:
#                 return False
#             stack.pop()
#         else:
#             stack.append(c)
    
#     return len(stack)==0

# s = "({([.])})"
# print(is_valid(s))


# def longest_pal(s):

#     res = ""

#     def expand(l,r):

#         while l>=0 and r<len(s) and s[l] == s[r]:

#             l -= 1
#             r += 1
        
#         return s[l+1:r]
    
#     for i in range(len(s)):

#         temp = expand(i,i)
#         if len(temp)>len(res):
#             res = temp

#         temp = expand(i,i+1)
#         if len(temp)>len(res):
#             res = temp
    
#     return res

# s = "ababba"
# print(longest_pal(s))