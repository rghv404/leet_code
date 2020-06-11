'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

 

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000

'''
import random
# this can be simply solve d by sorting the entire list (based on distncer from origin) and then return ing the first k points
# this is how I originaly  submitted it in LC. Time complexity is O(NlogN)
def kClosest(points: [[int]], K: int) -> [[int]]:
	ans = sorted(points, key = lambda coord: (coord[1]**2 + coord[0]**2))
	return ans[:K]

# I'll try to do it using quick select which on average would work in O(n) time 
def closerThanPivot(coord1: [int], coord2: [int]) -> bool:
	return (coord1[1]**2 + coord1[0]**2) < (coord2[1]**2 + coord2[0]**2)

def partition(lst:[[int]], start:int, end:int) -> int:
	pivot = lst[end]
	i = start
	for j in range(start, end):
		if closerThanPivot(lst[j], pivot):
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
	# at the end place the pivot at it's proper position
	lst[end], lst[i] = lst[i], lst[end]
	return i

def randPivot(lst, start, end) -> int:
	# this method selects a random number as pivot and replaces it with last elemet of the list to 
	# acehove both random pivoting and not fuck up the code
	print(start, end, "fro rand range")
	randPivot = random.randrange(start, end) if start > end else start # if condition cause for the edge case when single elements is being considered
	lst[randPivot], lst[end] = lst[end], lst[randPivot]
	return partition(lst, start, end)

def quickSelect(lst:[int], start:int, end:int, k:int) -> int:
	if start > end: return
	pi = randPivot(lst, start, end)
	print(pi)
	if pi == k - 1:
		return lst[:k]
	elif pi > k - 1:
		# select form left side
		return quickSelect(lst, start, pi - 1, k)
	return quickSelect(lst, pi + 1, end, k)


def kClosest_quickSelect(points: [[int]], K: int) -> [[int]]:
	return quickSelect(points, 0, len(points)-1, K)


arr = [[3,3],[5,-1],[-2,4]]
k = 2
res = kClosest_quickSelect(arr, k)
print(res)
