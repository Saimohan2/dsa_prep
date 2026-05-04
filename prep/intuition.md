s = "abcabcbb"

need to solve this using frequency map, every new element updates count of that element, when the frequency crosses 1, we keep deleting the elements from the left and reducing count.

at every valid state we calculate max and update it.

we need 2 variables, l(initialized outside) and r(r sits in for loop as r explores), both starting at index 0 r keeps checking the state and l keeps validating, shrinks boundary when the case is violated. when freq of certain element becomes 0 we delete that from freq map.

l = 0
f = {}
maxl = 0

for r in range(len(s)):
	
	f[s[r]] = f.get(s[r], 0)+1
	
	while f[s[r]]>1 and l<=r:
		f[s[l]] = f.get(s[l], 0) -1
		if f[s[l]] == 0:
			del f[s[l]]
		l += 1

	maxl = max(maxl, r-l+1)

return maxl

Given an array of positive integers nums and an integer k,
return the length of the longest subarray such that:

nums = [2,1,5,1,3,2], k = 7
Output: 4
Explanation: [1,5,1] or [5,1,1] etc.


This follows almost the same pattern too, r explores whats ahead as soon as the condition is valid, when the condition is invalid, need to shrink deducting l until the condition is valid again. Each valid case, maxl should be updated.

l = 0
maxl = 0
currsum = 0

for r in range(len(nums)):
	
	add nums[r] to currsum
	
	while currsum>k and l<=r:
		deduct nums[l] from currsum
		increment l
	maxl = maxl(maxl, r-l+1)

return maxl

Given an array of positive integers nums and integer k,
return the number of subarrays whose sum is ≤ k.

nums = [1,2,3]
k = 3

Output: 4

Valid subarrays:
[1], [2], [3], [1,2]

This problem is a bit different, here every element is also counted as a subarray, maintain currsum, explore with r shrink from l when condition invalidates, when condition becomes valid again, add tne length to count. this gives all the possible subarrays, instead of just the count.

l = 0
count = 0
currsum = 0

for r in range(len(nums)):

	currsum = currsum + nums[r]
	
	while the running sum is greater than k and l doesnt pass r:
		currsum minus nums[l]
		increment l
	
	count = count + length of the subarray

return count

Given a string s and integer k, return the length of the
longest substring with at most k distinct characters.

s = "eceba"
k = 2

Output: 3  # "ece"

My first intuition for this problem was to maintain a set and measure the length at every iteration, but it silently fails in conditions like "aaabdcd", in this case, when a is deleted, no frequency is stored, we dont want that we need a freq map which carries the count of element in that substr, such that we can keep deleting. Thinking time.

dry run with set case:

set.add(a)
set.add(a)
set.add(a)
set.add(b)
set.add(c)
set.add(d) distinct becomes 4
when we suddenly perform
set.remove(a), then increment l, we are still at 1st index and its again a, but we lost a from the set. No ideal case. Hence in this place, we maintain a freq map and track the len of it, when length violates, remove l element frequency and check if freq of l becomes 0 and finally delete it, when the len of freq satisfies again, it exits loop and we track the length of that sub str.

l = 0
freq = {}
maxl = 0

for r in range of length of s:
	add or increase the count of element's freq
	
	while len of freq is > k and l is behind r:
		minus the count of l element in freq
		check if it becomes 0 and delete it
		increment l
	update max if new max arrives
return maxl