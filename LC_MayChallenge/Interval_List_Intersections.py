'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

 

Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

def intervalIntersection_clunky(A: [[int]], B: [[int]]) -> [[int]]:
	
	def getIntersectPair(first:[int], second:[int]):
		if first[1] < second[0]: #interval before
			return None, True
		elif first[0] > second[1]: # interval before or after
			return None, False
		ansMin = max(first[0],second[0])
		ansMax = min(first[1], second[1])
		return ansMin, ansMax

	i, startPoint = 0, 0
	ans = []
	while i < len(A):
		j = startPoint
		while j < len(B):
			ansPair = getIntersectPair(A[i], B[j])
			print(A[i], B[j], ansPair)
			if ansPair[1] and ansPair[0] is None:
				# disjoint pair, keep iterating A array
				# if B pair is before A pair then next A pair should not compare from the start of B pair
				startPoint = j - 1 if j > 0 else 0
				break
			elif ansPair[0] is not None:
				ans.append(list(ansPair))
			j += 1
		i += 1
	print(ans)

# the above code can be improved as follows, doing bascially the same thing but in a more clearner code style
def intervalIntersection(A: [[int]], B: [[int]]) -> [[int]]:
	i, j, ans = 0, 0, []
	while i < len(A) and j < len(B):
		first, second = A[i], B[j]
		print(first, second)
		ansMin = max(first[0], second[0])
		ansMax = min(first[1], second[1])

		if ansMin <= ansMax:
			ans.append([ansMin, ansMax])

		# if A[i] ends before B[j] then increment i cause it won't have a subset after j
		if first[1] < second[1]:
			i += 1
		else:
			j += 1 # else keep checking with next B pair

	print(ans)

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

A = [[0,5],[12,14],[15,18]]
B = [[11,15],[18,19]]

A = [[0,4],[7,8],[12,19]]
B = [[0,10],[14,15],[18,20]]
intervalIntersection(A, B)
