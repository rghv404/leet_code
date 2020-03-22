'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''


def combinationSum(candidates: [int], target: int) -> [[int]]:
	if not candidates:
		return []

	def dfs_1(arr:[int], subSet: [int], target:int, start:int):
		nonlocal res
		if sum(subSet) == target:
			res.append(subSet)
			return
		for i in range(start, len(arr)):
			if sum(subSet) + arr[i] > target:
				continue # continue because no guiratnee if the arr is sorted or not if it is we can use break here
			# we'll no increase start untill the dfs is complete witht he current item in arr
			dfs_1(arr, subSet + [arr[i]], target, i)

	# another way to traverse is not hceking the sum but keep reducing the target and when it becomes 0 then append the subset
	def dfs_2(arr:[int], subSet: int, target:int, start:int):
		nonlocal res
		
		if target == 0:
			res.append(subSet)
			return
		for i in range(start, len(arr)):
			if arr[i] > target: 
				break
			dfs_2(arr, subSet + [arr[i]], target - arr[i], i)

	res , currSet = [], []
	dfs_1(candidates, currSet, target, 0)
	return res

arr = [6,2,3,7]
# arr = [2,3,5]
res = combinationSum(arr, 7)
print(res)

# in below problem a candidate can only be considered once
def combinationSum_2(candidates: [int], target: int) -> [[int]]:
	def dfs(arr:[int], subSet:[int], target: int, start:int, res: [[int]]):
		if target == 0:
			res.append(subSet)
			return res
		for i in range(start, len(arr)):
			if arr[i] > target:
				break
			if i > start and arr[i] == arr[i-1]:
				continue
			dfs(arr, subSet + [arr[i]], target - arr[i], i + 1, res)
		return res

	candidates.sort()
	res = dfs(candidates, [], target, 0, [])
	return res


arr = [10,1,2,7,6,1,5]
# arr = [2,5,2,1,2]
res = combinationSum_2(arr, 8)
print(res)

def permute(nums:[int])-> [[int]]:
	def dfs(nums:[int], subSet:[int], n:int, res:[[int]])-> [[int]]:
		if len(subSet) == n:
			res.append(subSet)
		for i in range(len(nums)):
			num = nums[i]
			restArray = nums[:i] + nums[i+1:]
			dfs(restArray, subSet + [num], n, res)
		return res

	# res = []
	res = dfs(nums, [], len(nums), [])
	return res

# below is when there are duplicate numbers allowed in teh list but we dont' want them in paermutaions
def permute_2(nums: [int])-> [[int]]:
	def dfs(nums: [int], n:int, subSet:[int]) -> [[int]]:
		nonlocal res
		if len(subSet) == n:
			res.append(subSet)
			return
		for i in range(len(nums)):
			num = nums[i]
			restArray = nums[:i] + nums[i+1:]
			if subSet + [num] + restArray in res:
				continue
			dfs(restArray, n, subSet+[num])
		# return res
	res = []
	dfs(nums, len(nums), [])
	return res
	

arr = [1,1,2,3]
res = permute_2(arr)
print(res)