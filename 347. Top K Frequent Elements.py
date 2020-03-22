'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
from datetime import datetime

def topKFrequent(nums: [int], k: int) -> [int]:
	count_bucket = dict()
	for num in nums:
		count_bucket.setdefault(num, 0)
		count_bucket[num] += 1
	print(count_bucket)
	sorted_dict = sorted(count_bucket.items(), reverse=True,key=lambda x: x[1])
	print(sorted_dict)
	return [tup[0] for tup in sorted_dict]

res = topKFrequent([1,1,1,2,2,3], 2)
print(res)

def topKproductsLastHour(prdTuple:tuple, k: int) -> [str]:
	# we store products in dictionary 
	product_bucket = dict()
	currTime = 11

	for product_name, timeStamp in prdTuple:
		product_bucket.setdefault(product_name, 0)
		if timeStamp >= currTime - 1 and timeStamp <= currTime:
			product_bucket[product_name] += 1 
	# sort the collection using the values for each key
	print(product_bucket)
	sorted_count_bucket = sorted(product_bucket.items(), reverse=True,key = lambda x : x[1])
	print(sorted_count_bucket)
	return [productId for productId, _ in sorted_count_bucket[:k]]

ip = [("p1", 10), ("p1", 10.5), ("p1", 10.2), ("p2", 10), ("p2", 10.7), ("p2", 10.5), ("p3", 10)]
res = topKproductsLastHour(ip, 2)
print(res)