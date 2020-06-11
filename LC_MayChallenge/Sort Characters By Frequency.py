'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''
import collections
# below solution uses eveyr python way possible. The complexisty is stil o(Nlogn) and O(n) for space
def frequencySort(s: str) -> str:
        # create a collections bucket and then sort
        countBucket = collections.Counter(s)
        # print(countBucket)
        sortedS = sorted(s, key=lambda x: (-countBucket[x],x))
        return ''.join(sortedS)


# if we don't want to passs the second key inside the sort, we can sort the bucek tby key and then build the string 
# by doing  a porduc of key and val as we iterate through sorted dictionary
# this solution also takes O(nlogn) time 
def frequencySort_sortDict(s: str) -> str:
        # create a collections bucket and then sort
        ans = ''
        countBucket = collections.Counter(s)
        # print(countBucket)
        for key, val in countBucket.most_common():
        	ans += val*key
        return ans
        # sortedS = sorted(s, key=lambda x: (-countBucket[x],x))
        # return ''.join(sortedS)


# another method to do it in linear time is to create count bukcet and then sort using bucket sort method
# thjis s possible cause we know the upper bound of any letter count will be n i.e. len(string)
def frequencySort_bucektSort(s: str) -> str:
        # create a collections bucket and then sort
        ans = ''
        countBucket = collections.Counter(s)
        # now create an array of len of stirng
        arr = [[] for _ in range(len(s))]
        print(arr)
        for k, val in countBucket.items():
        	arr[val].append(k)

        print(arr)
        # now iterate through above array from the end and create string if arr slot is not empty
        i = len(arr) - 1
        while i >= 0:
        	if arr[i]:ans += ''.join(i*arrVal for arrVal in arr[i])
        	i -= 1
        return ans
   

ip = 'welcometoleetcode'
res = frequencySort(ip)
res = frequencySort_sortDict(ip)
res = frequencySort_bucektSort(ip)
print(res)