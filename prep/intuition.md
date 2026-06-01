## s = "abcabcbb"

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

## Given an array of positive integers nums and an integer k,
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

## Given an array of positive integers nums and integer k,
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

## Given a string s and integer k, return the length of the
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

## Given a string s and integer k,
## return the number of substrings with exactly k distinct characters.

s = "pqpqs"
k = 2

Output: 7

Exactly k: its hard to calculate it with a regular sliding window. So we can do atmost k - atmost k-1. which leaves with k.

l = 0
f = {}
count = 0

for r in range(len(s)):
	add right element to the freq map and increase count

	while len of f > k:
		decrease the left element count by one to shrink window
		check if count = 0
			delete f of l element
		increment l
	
	calculate count
return count

## Given an integer array nums, return the maximum subarray sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]
Output = 6  # [4,-1,2,1]

If asked in array of positive numbers, we can clearly say that the max subarray sum will be
 the sum of all elements, but with negative numbers, the scenario shifts. The reason behind 
 is, a negative number may destroy the current best sum, so every time we must decide on two 
 things, whether to continue the current state by adding coming number to it or just tsart 
 the state from current element. Ex: adding 4 to -2 kills 4's sum, as we're chcking for max, 
 we will start afresh from 4 instead of adding it to -2. Kadane says, while finding max, 
 chose the best at every step. We dont need two pointers, we take a greedy approach that we might find something good later, so we run it through the loop and pick best at every time.

 currsum = 0
 maxs = 0

 for i in range of len of nums:
	
	currsum = max(current element, currsum+current element)

	maxs = max(currentsum, maxs)
return maxs

## Find the maximum subarray sum after at most one deletion

nums = [5, -1, -2, 10]
expected: 15

here we do kadane and we choose to either continue with the last cursum using one more option called drop, we initialise drop to 0 which means we're aiming with 1st element deletion at the start, in a greedy approach, we check last kept kadane cursum, to compare it
with drop's state change if one more element adds to drop.

keep(which is nothing but currsum) = 1st element
drop = 0(ignoring 1st element here)
maxs = 1st element

for i in range of len of nums:

	drop = max(keep, drop+nums[i])
	keep = max(curelement, keep+curelement)

	maxs = max(maxs, keep, drop)

return maxs

## Given a sorted array nums and an integer target, return True if there exists a 
## pair(i, j) such that:

nums = [1, 2, 3, 4, 6]
target = 6

Output: True   # because 2 + 4 = 6

This is quite easy and straight forward, in a sorted lost, the bigger numbers exist to the right and smaller numbers exist to the left, so if sum exceeds target, shrink r, if sum is
small, shrink l.

l = 0
r = len-1

while l<r
	if nums[l]+nums[r]>target:
		decrease r
	elif nums[l]+nums[r]<target:
		increase l
	else:
		return true
if nothing catches return false

## Given an unsorted array, return indices such that: nums[i] + nums[j] == target

nums = [2, 7, 11, 15]
target = 9

Output: [0, 1]

Given the array is unsorted, we cant follow two pointer approach, as we cant decide the 
direction blindly. Hence we store result in hashmap, with element as key and index as value.
Then at each element, we subtract element from the target, if a complement found in the 
hashmap, then we return the indeces.

m = {}

for i in range of len(nums):

	comp = target - element
	if comp in map:
		return [map[comp], i]

	add element to map
return []

## Given a string s, return the length of the longest substring without repeating characters.

s = "abcabcbb"
Output = 3   # "abc"

again a frequency tracking pattern, we use left and right pointers, right pointer is dynamic, while left contains valid boundary. As case becomes invalid i.e., freq goes past 1 of an entering r element, the freq of l should be decremented, deeted if 0 and moved on to next l. After every valid step, recompute maxl.

l = 0
maxlen = 0
n = len
f = {}

for r in range of n:

	add r to freq/increment the count

	check validity(while f{r}>1):
		decrease s[l] count, to lose it from the state
		check if the l freq becomes 0:
			delete it from f
		increment l

	update maxlen
return maxlen

## Given an array of positive integers nums and integer k,
return the length of the longest subarray such that: sum<=k

nums = [2,1,5,1,3,2]
k = 7
Output = 3

explore from right, add it to currsum, when invalid keep shrinking from l, update max.

l = 0
maxl = 0
cursum = 0

for r inr range of len:
	cursum = cursum + r
	while sum>k:
		subtract l from sum
		increment l
	update max
return max

## Given an array nums, return all unique triplets
## such that: nums[i] + nums[j] + nums[k] == 0

nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2],
 [-1,  0, 1]]

This problem doesn't need to return indeces, so we just have to verify whether there's 
possibility or not. First we haver to sort nums, then for each num, we check two sum
condition for the numbers that are remaining, then each iteration, we check whether they are
adding to zero, if not we increment l and r by the condition, if validity succeeds, we append
those numbers to the res array.

-4, -1, -1, 0, 1, 2

-4 -1 2 -3<
-4 0 2 -2<
-4 1 2 -1

res = []

sort nums

for i in range of len:

	l = i+1
	r = len-1

	while nums of l l = l+1
		l = l+1
	while nums of r = r-1
		r = r-1
	

	while l<r:

		if i + l+r<0:
			incr l
		
		elif i+l+r>0:
			decr r
		else:
			append i,l,r to res

return res

## Given an array nums, for each element, find the next greater element to its right.
If none exists, return -1.

nums = [2,1,2,4,3]

Output = [4,2,4,-1,-1]

this is done by monotonic stack implementation, first we in initialize a res with -1s, and 
an empty stack, as iterate through every element, we add element to top of stack.

res = [-1]*len(nums)-1
stack = []

for i in rnage of len(nums):
	while stack is not empty and current element is greater than stack's top:
		res[stacktopindex] = current_element
		stack.pop()
	
	stack.append(i)
return res


## Given an array of integers temps where: temps[i] = temperature on day i
## Return an array res such that: res[i] = number of days you have to wait after day i to get a 
warmer temperature

## If there is no future day with a warmer temperature, set: res[i] = 0
temps = [73,74,75,71,69,72,76,73]

Output = [1,1,4,2,1,1,0,0]

this is again a monotonic stack implementation and comparing the stack top element with current 
temperature to check if it is the release element to the elements in the stack. Once a higher 
temperature is found, we compute the difference between top element and the current i before popping
the top element and store it in the result array, if an element has no higher temperature in the 
array ahead, we leave its result as 0.

res = [0]*len(temps)
stack = []

for i in range of len of temps:

	while stack is not empty and current temperature is > stack's last index's element in temp:
		
		res[stack[-1]] = i-stack[-1]
		stack.pop()
	
	stack.append(i)
return res

## Given a sorted array nums and a target,
## return the index of target. If not found → return -1

nums = [-1,0,3,5,9,12]
target = 9

Output = 4

as this is sorted, binary seach works for this problem, in binary search, we initialise l to 0,
r to len(nums)-1 and mid is basically l+r//2. If the mid element is greater than target, target
would be in the left part so we set r to mid-1 and then update mid in the start of loop until 
target is found, when found then we can return mid value from there. When not found, we return -1 
at last.

l = 0
r = len(nums)-1

while l<=r:
	mid = l+r//2

	if nums[mid]>target:
		r = mid-1
	elif nums[mid]<target:
		l = mid+1
	else:
		return mid
return -1

## You are given an array: piles = [3,6,7,11] Each element represents a pile of bananas.
## You are also given an integer: h = 8 which represents the number of hours Koko has
## to finish eating.
## 
## Rules:
## Koko eats at a constant speed of k bananas per hour.
## Each hour, she chooses one pile and eats up to k bananas.
## If a pile has fewer than k bananas, she eats all of it and stops for that hour.
## 
## Return the minimum integer k such that Koko can finish all bananas within h hours.

this is a tricky problem, we have to use binary serach on answer, for intuition, it has 
stated that at any given speed, if the koko has finished eating bananas in that pile before 
an hour, she has to wait idle for the entire hour before jumping to next pile, which allows 
us to think that max eating speed would be max bananas in a pile: lets say if there are 3 
bananas in a pile and koko has speed of 5/hr then she'd finish 3 bananas and wait for the 
hour to be completed, if max pile is 8 and we use speed 10 she can finish those bananas in 
len(piles) hours. Max is unbounded, speed greater than max pile will always lead to same 
result, so we take max speed as max pile bananas. So we take l as 1(minimum speed as there 
will be atleast 1 banana in a pile or even if there are 0 koko will wait until the hour 
passes) and r as max pile. At every iteration we assign mid as k and check the time it takes 
to finish those piles using a helper function, there we implement the binary search. When 
hours taken are more than allotted hours, we assign l to mid+1 if less than or equal, that 
satisfies condition and we assign answer as mid and decrease r to find if any speed to
left satisfies the condition as we need to find minimum speed.

hours_taken func:
	thours = 0

	for p in piles:
		thours = hours+ceil(p/k)(ceil because, if she finishes fast, she'll wait to round the hour)
	
	if thours<=hours_needed:
		return True
	else:
		return False

min_speed:
	l = 1
	r = max(piles)

	while l<=r:

		mid = (l+r)//2

		if hours_taken(mid) is true:
			answer = mid
			r = mid-1
		else:
			l = mid+1
	return answer

## Given an array nums and an integer k,
## return the number of subarrays whose sum equals k.
## 
## nums = [1,1,1]
		   0,1,2
## k = 2
## 
## Output = 2

this can be solved by prefix sum logic, any subarray sum from i-->j would be equal to
prefsum[j]-prefsum[i-1], which means, if we subtract that subarray sum from pref[j] gives us
value of pref[i-1], so at any point when we do pref[j]-k it should give us prefix till i-1.
Hence we keep checking pref[j]-k at every step and verifying if we've ever seen pref till i-1
ever, if seen, that means that sum from i-1 to j would be k.

count = 0
seen = {0:1}
cursum= 0

for i in range of len of nums:

	if pref[j]-k in seen:
		count = count + seen[pref[j]-k]
	seen[cursum] = seen.get(cursum, 0)+1
	
	return count

## Given an integer array nums and an integer k,
## return the length of the longest subarray whose sum equals k.
 
## nums = [1, -1, 5, -2, 3]
## k = 3

## Output = 4

unlike the previous problem, we store the first occurence of every prefsum, so later when 
its found again, we can compute the max.

seen = {0:-1}
maxlen = 0
currsum = 0

for i in range of l of nums:

	if currsum-k in seen:
		len = i-seen[currsum-k]
	
	else:
		seen[currsum] = i
	
	maxlen = max(maxlen, len)
return maxlen