''' Given an array of integers and an integer k, you need to find the number
of unique k-diff pairs in the array. Here a k-diff pair is defined as an
integer pair (i, j), where i and j are both numbers in the array and their
absolute difference is k. 

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

'''	



def findPairs_TLE(nums: [int], k: int) -> int:
	if not nums:
		return 0

	count = 0	
	ansSet = set()
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if abs(nums[i] - nums[j]) == k and ((nums[i], nums[j]) or (nums[j], nums[i]) not in ansSet):
				ansSet.add((nums[i], nums[j]))
				count += 1
	return count


def findPairs_mySol(nums:[int], k:int) -> int:
	if not nums or k < 0:
		return 0

	# create a dict for nums
	bucket = {}
	for i, num in enumerate(nums):
		bucket.setdefault(num, set()).add(i)

	seen_pairSet = set()
	count = 0
	print(bucket)
	# enumerate each num in orig array and check if it's targfet num is present
	for currNum in nums:
		target = currNum - k
		# handling k = 0 and finding second pair here
		if target in bucket and (target != currNum or len(bucket[target]) > 1):
			pair = (currNum, target) if currNum < target else (target, currNum)
			if pair not in seen_pairSet:
				seen_pairSet.add(pair)
				count += 1
		print(seen_pairSet)
	return count

'''
Note: We actually don't need seenSet if we're going through the collection keys rather than the array
This solution also takes O(n) tiem and O(n) space
'''
import collections
def findPairs(nums:[int], k:int) -> int:
	if not nums or k < 0:
		return 0
	count = 0
	bucket = {}
	for num in nums: # no need for havign s set of indexes cause caounter will work
		if num not in bucket:
			bucket[num] = 1
		else:
			bucket[num] += 1

	for key in bucket:
		target = key - k
		print(key, target)
		if (target == key and bucket[target] > 1) or (target!=key and target in bucket):
			count += 1
	return count


'''
Another two pointer approach is to sort the array and use two pointers to find the pairs
This takes O(nlogn) time and O(1) space
'''
def findPairs_twoPntrs(nums:[int], k:int) -> int:
	if not nums or k < 0:
		return 0
	# sort the array
	nums.sort()
	count = 0
	start, end = 0, 1
	while start < len(nums) and end < len(nums):
		# if start + k is m,ore than end than we need to move end to right by 1
		if start == end or nums[start] + k > nums[end]:
			end += 1
		elif nums[start] + k < nums[end]:
			start += 1
		else: # equality found
			count += 1
			start += 1
			while end + 1 < len(nums) and nums[end] == nums[end+1]:
				end += 1
			end += 1

	return count

ip = [3,1,4,1,5]
ans = findPairs_twoPntrs(ip, 0)
print(ans)