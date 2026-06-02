"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome reads the same forward and backward.

Input: s = "racecar"
Output: true

Input: s = "hello"
Output: false

"""

# def ispal(s):

#     l = 0
#     r = len(s)-1

#     while l<=r:

#         if s[l] == s[r]:
#             l = l+1
#             r = r-1
        
#         else:
#             return False
    
#     return True

# s = input("Enter a string")
# print(ispal(s))

"""
Given a string s, return true if it can become a palindrome after deleting at most one character,
otherwise return false.

Input: "abca"
Output: true

Input: "abc"
Output: false

"""

# def is_pal(s, l, r):

#     while l<=r:
        
#         if s[l]!=s[r]:
#             return False
        
#         l += 1
#         r -= 1

#     return True

# def is_validpal(s):

#     l = 0
#     r = len(s)-1

#     while l<=r:

#         if s[l] != s[r]:

#             return(is_pal(s, l+1, r) or
#                    is_pal(s, l, r-1))

#         l += 1
#         r -= 1
    
#     return True

# s = "abcaa"
# print(is_validpal(s))

# s = "A man, a plan, a canal: Panama"

# joined = list(s)

# x = [str.lower(l) for l in joined if l.isalnum()]

# x = "".join(x)

# print(x)

"""
Given a string s, determine whether it is a palindrome considering only alphanumeric characters 
and ignoring cases.

Input: "A man, a plan, a canal: Panama"
Output: True

"""

# def is_pal(s):

#     s = list(s)

#     a = [str.lower(l) for l in s if l.isalnum()]

#     a = "".join(a)

#     l = 0
#     r = len(a)-1

#     while l<r:

#         if a[l] != a[r]:
#             return False
        
#         l += 1
#         r -= 1

#     return True

# s = "A man, a plan"
# print(is_pal(s))

"""
Given a sorted integer array nums, remove the duplicates in-place such that 
each unique element appears only once.

Return the number of unique elements k.

The first k positions of nums should contain the unique elements.

Input:
nums = [1,1,2]

Output:
k = 2

nums becomes:
[1,2,_]
"""

# def unique(nums):

#     left = 0

#     for right in range(1, len(nums)):

#         if nums[right] != nums[left]:

#             left += 1

#             nums[left], nums[right] = nums[right], nums[left]

#     return left+1

# nums = [1,1,2,3,3,5,5]
# print(unique(nums))

"""
Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in-place.

Return the number of remaining elements.

nums = [3,2,2,3]
val = 3

Output: 2

nums becomes:
[2,2,_,_]
"""

# def rem_val(nums, val):

#     l = 0

#     for r in range(len(nums)):

#         if nums[r] != val:

#             nums[l], nums[r] = nums[r], nums[l]

#             l = l+1

#     return nums

# nums = [3,2,3,2,3,2,3]
# val = 3

# print(rem_val(nums, val))

"""
Move Zeroes

Given an integer array nums, move all 0s to the end while maintaining the relative order of the 
non-zero elements.

You must do this in-place.

Input:
[0,1,0,3,12]

Output:
[1,3,12,0,0]

"""

# def move_zeroes(nums):

#     l = 0

#     for r in range(len(nums)):

#         if nums[r]!=0:

#             nums[l], nums[r] = nums[r], nums[l]

#             l += 1
    
#     return nums

# nums = [1,0,2,3]
# print(move_zeroes(nums))

"""
Squares of a Sorted Array

Given a sorted array nums in non-decreasing order, return an array of the squares of each number, 
also sorted in non-decreasing order.

Input:
[-4,-1,0,3,10]

Output:
[0,1,9,16,100]

"""

# def sort_sq(nums):

#     res = [0]*len(nums)

#     l = 0
#     r = len(nums)-1
#     write = len(nums)-1

#     while l<=r:

#         if abs(nums[l])>abs(nums[r]):

#             res[write] = nums[l]**2

#             l += 1
#             write -= 1
        
#         else:

#             res[write] = nums[r]**2
#             r -= 1
#             write -= 1

#     return res

# nums = [-4,-1,0,3,10]
# print(sort_sq(nums))