'''
The idea is to return the kth smallest or largest element 
by sorting upuntil that index.
Also we iterate over only the needed half of the list
'''
def partition(lst:[int], start:int, end:int) -> int:
	# lastg elem as pivot
	pivot, pvIndex = lst[end], start - 1
	print(lst, pivot)
	for j in range(start, end):
		if lst[j] < pivot:
			pvIndex += 1
			lst[j], lst[pvIndex] = lst[pvIndex], lst[j]
	# replace pivot at end to it's final desired location
	lst[end], lst[pvIndex+1] = lst[pvIndex+1], lst[end]
	return pvIndex+1


def quickSelect(lst:[int], start:int, end:int, k: int) -> [int]:
	if start > end:
		return
	pi = partition(lst, start, end)

	if pi == k-1:
		return lst[:k]
	elif pi > k - 1:
		quickSelect(lst, start, pi-1, k)
	else:
		quickSelect(lst, pi + 1, end, k)

ip = [7,5,3,1,2,4]
res = quickSelect(ip, 0, len(ip)-1, 4)
print(res)