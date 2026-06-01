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