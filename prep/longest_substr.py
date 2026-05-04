"""
Problem:
Given a string s, find the length of the longest substring 
without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: "abc"
"""

def longest_subs(s):

    l = 0
    f = {}
    maxl = 0
    n = len(s)

    for r in range(n):

        f[s[r]] = f.get(s[r], 0) +1

        while f[s[r]]>1 and l<=r:

            f[s[l]] = f.get(s[l], 0) -1

            if f[s[l]] == 0:
                del f[s[l]]
            
            l = l+1
        maxl = max(maxl, r-l+1)
    return maxl

s = "abcaaaaa"
print(longest_subs(s))


"""
Given an array of positive integers nums and an integer k,
return the length of the longest subarray such that:

nums = [2,1,5,1,3,2], k = 7
Output: 4
Explanation: [1,5,1] or [5,1,1] etc.
"""

def max_len(nums, k):

    l = 0
    maxl = 0
    currsum = 0

    for r in range(len(nums)):
        currsum += nums[r]

        while currsum>k and l<=r:
            currsum = currsum - nums[l]
            l += 1
        
        maxl = max(maxl, r-l+1)
    
    return maxl

nums = [2,1,5,1,3,2]
k = 7

print(max_len(nums, k))

"""
Given an array of positive integers nums and integer k,
return the number of subarrays whose sum is ≤ k.

nums = [1,2,3]
k = 3

Output: 4

Valid subarrays:
[1], [2], [3], [1,2]
"""

def count_sub(arr, k):

    l = 0
    currsum = 0
    count = 0

    for r in range(len(arr)):
        currsum += arr[r]

        while currsum>k and l<=r:
            currsum -= arr[l]
            l += 1

        count += r-l+1

    return count

arr = [3,1,0]
k = 3
print(count_sub(arr, k))

"""
Given a string s and integer k, return the length of the
longest substring with at most k distinct characters.

s = "eceeeba"
k = 2

Output: 3  # "ece"
"""

def distinct_char(st, k):

    l = 0
    maxlen = 0
    f = {}

    for r in range(len(st)):
        f[st[r]] = f.get(st[r], 0)+1

        while len(f)>k and l<=r:
            f[st[l]] = f.get(st[l], 0)-1
            if f[st[l]] == 0:
                del f[st[l]]
            
            l += 1
        
        maxlen = max(maxlen, r-l+1)
    
    return maxlen

st = "eceeeeeba"
k = 2

print(distinct_char(st, k))