# let's see wha the question is
# enocoded string, number represents how many time the character appears in the row
# i1s2


def function(lst):
    if lst is None:
        return []
    res = ''
    i = 0
    while i <= len(lst) - 1:
        occur = int(lst[i + 1])
        res += ''.join(lst[i] for j in range(occur))
        i += 2
    print(res)
    return res

# sum of all of it's factors excluding



def func3(lst):
    # evaluate everything from left to right
    # convert string to math opertaion and evaluate
    # 1 plus 2 * 3
    # use stack to store operators
    operators

res = function("i1s2b3h5j7")
