''''
Have probably done this few hundred times but still fkin forget the dfs logic
trying hwere after a dry run of a seen cdoe
possibly try further
'''

def permute(arr:[str])-> [str]:
	# boundary case: when no array
	if not arr:
		return
	# bvase case: single elemnet in array -> return single elem list
	if len(arr) == 1:
		return [arr]

	# init your op list
	ret = []

	# iterate the original list and for each item permute on rest of list
	for i, item in enumerate(arr):
		remList = arr[:i] + arr[i+1:]
		for comb in permute(remList):
			ret.append([item] + list(comb))
	return ret


res = permute([1,2,3,4])
print(res)