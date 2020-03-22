'''
A basic recursive implementation of quickSort Algo
'''
def partition(lst, start, end):
	# choose pivot to be last
	pivot = lst[end]
	i = start
	for j in range(start, end):
		# compaer each elemnt to pivot; if less than repalce 
		# with what will be final pivotLocation
		if lst[j] < pivot:
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
	# swap pivot element to it's desired location
	lst[i], lst[end] = lst[end], lst[i]
	# return pivot locatio
	return i

def quickSort(lst, start, end):
	# we first partition the passed list
	if start < end:
		# parititon such that pi is at correct position
		pi = partition(lst, start, end)

		# sort left side
		quickSort(lst, start, pi-1)
		# sort right
		quickSort(lst, pi+1, end)
	return lst

ip = [4,5,6,1,3,2]
res = quickSort(ip, 0, len(ip)-1)
print(res)

