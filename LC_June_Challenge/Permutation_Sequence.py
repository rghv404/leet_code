''''The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

'''

def getPermutation(n: int, k: int) -> str:
	# generate all perms and return kth ? doesn't work
        # first of all backtracking solution doesn't give value in order of permutaion generated
        # the other solution where wetake a number and then append it to permuted list gives permutaion in order bu does not work here because of TLE
        # the thirs and final solution ises a factorial number system represetaion for each permuation label so kth permuation of 4 will be represenation by factoiral number as 4 = 0*3! + 2*2! + 0*1! + 0*0!
        # once this represenation si generated we take the k*m! k as index of number list and keep deletign that index to regen the array so we'll use 0th index of 0*3! i.e. nums[0], pop 0 and then use 2 from 2*2! then pop 2 then use 0 and pop and 0 and pop to make 1423.
        
        # create factorial and array list
        fct, nums = [1], ["1"]
        for i in range(1, n):
            fct.append(fct[i-1]*i)
            nums.append(str(i+1))
        print(fct, nums)
        k -= 1 # to make k aligned to zero index approach cause 0th index holds the 1st permutaion and so on
        res = ""
        for i in range(n-1, -1, -1):
            idx = k // fct[i]
            k -= idx * fct[i]
            res += nums[idx]
            del nums[idx]
        return res

# the other solution wchich you can practically come up wiuth in the interview is
# to take a number and then permute on the rest of list and append this number to this perm
def getPermutation_nFact(n:int, k:int) -> str:
    return

res = getPermutation(4,8)
print(res)