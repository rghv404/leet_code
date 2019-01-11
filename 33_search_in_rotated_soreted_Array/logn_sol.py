class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # my idea rotate back teh array from teh pivot,
        # the max element is the pivot key 
        # chcek if the max element is the last or not , if it's last then array is not pivoted
        # else shift all items before max including max to the end of the arra
        # nums.sort()
        # return binsearch(nums, target)
        l, r = 0, len(nums) - 1
        # return binsearch(nums, target)
        return rotatedsearch(nums, l, r, target)

# below binary search does not actually take log n time cause of the slicing array passed
# slicing of the array itself 
# def binsearch(a, target):
#     mid = len(a)//2
#     if len(a) == 0:
#         return -1
#     if a[mid] == target:
#         return 1
#     else:
#         if target > a[mid]:
#             print(a[mid])
#             print('Greater, ging into', a[mid+1:])
#             return binsearch(a[mid+1:], target)
#         elif target < a[mid]:
#             print(a[mid])
#             print('Lesser, gopign into', a[:mid])
#             return binsearch(a[:mid], target)

def rotatedsearch(arr, l, r, key):
    mid = (l +r) // 2
    
    if l>r:
        return -1
    
    if arr[mid] == key:
        return mid
    
    if arr[l] <= arr[mid]:
        # first considering that the left side is sorted
        # we search our element in this half or the other half depending on where it lies
        if arr[l] <= key and arr[mid] >= key:
            return rotatedsearch(arr, l, mid-1, key)
        return rotatedsearch(arr, mid+1, r, key)
        
    # if above condition is not true it means that the second half of the array ios sorted
    # thus we performa the same search in that half
    if arr[mid] <= key and arr[r] >= key:
        return rotatedsearch(arr, mid+1, r, key)
    return rotatedsearch(arr, l, mid-1, key)

# below is basic bianry search  (log n) for reference 
def binsearch(a, target):
    l, r = 0, len(a) - 1
    index = -1
    while l<=r and index == -1:
        m = (l + r) //2
        if a[m] == target:
            index = m
        else:
            if target > a[m] and a[r] > target:
                l = m + 1
            else:
                r = m - 1
    return index