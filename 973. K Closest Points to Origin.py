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

class Solution:
    def partition(self, lst: [int], start: int, end: int) -> int:
        pivot, _, _ = lst[end]
        pvIndex = start
        for i in range(start, end):
            if lst[i][0] < pivot:
                lst[pvIndex], lst[i] = lst[i], lst[pvIndex]
                pvIndex += 1
        lst[pvIndex], lst[end] = lst[end], lst[pvIndex]
        # print(pvIndex, lst)
        return pvIndex
                 
    def quickSelect(self, lst:[int], start:int, end:int, k:int) -> [int]:
        if start > end:
            return
        pi = self.partition(lst, start, end)
        if pi == k-1:
            return [[x,y] for _, x, y in lst[:k]]
        elif pi > k - 1:
            return self.quickSelect(lst, start, pi - 1, k)
        else:
            return self.quickSelect(lst, pi + 1, end, k)
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # done with heapify(O(N)+O(kLOGN) and o(NLOGN) - using dic tand sorting
        # trying average O(N) solution uisng quickSelect
        lst = []
        for x, y in points:
            eucDst = x ** 2 + y ** 2
            lst.append((eucDst, x, y))
        return self.quickSelect(lst, 0, len(lst) - 1, k)
        